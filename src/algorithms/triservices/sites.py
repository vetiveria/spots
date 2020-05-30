import math

import dask.dataframe as dd
import numpy as np

import src.algorithms.triservices.api
import src.algorithms.triservices.settings
import src.functions.geodetic


class Sites:

    def __init__(self):

        api = src.algorithms.triservices.api.API()
        self.url = api.url()

        settings = src.algorithms.triservices.settings.Settings()
        self.fields, self.names, self.types = settings.getattributes()
        self.stringfields = settings.getstringfields()

        self.kwargs = {'usecols': self.fields, 'header': 0, 'encoding': 'UTF-8',
                       'sep': ',', 'dtype': self.types}

    def read(self, source):

        try:
            # data = pd.read_csv(filepath_or_buffer=source, header=0, sep=',',
            #                    usecols=self.fields, dtype=self.types, encoding='UTF-8')
            data = dd.read_csv(urlpath=source, blocksize=32000000, **self.kwargs)
        except OSError as err:
            raise ('OS Error {0}'.format(err))

        return data.rename(columns=self.names)

    def format(self, blob: dd.DataFrame):

        data = blob.copy()
        for field in self.stringfields:
            data[field] = data[field].fillna(value='')

        return data

    @staticmethod
    def getcoordinates(blob: dd.DataFrame):

        data = blob.copy()
        geodetic = src.functions.geodetic.Geodetic()

        for field in ['FAC_LATITUDE', 'FAC_LONGITUDE']:
            data[field.strip('FAC_')] = data[field].apply(
                lambda x: geodetic.geodetic(x) if not math.isnan(x) else np.nan,
                meta=(field, 'float64'))

        return data.drop(columns=['FAC_LATITUDE', 'FAC_LONGITUDE'])

    def getquery(self, blob: dd.DataFrame):

        blob['query'] = blob.FACILITY_NAME + ' ' + blob.STREET
        for field in ['CITY', 'STUSPS', 'ZIP_CODE']:
            blob['query'] = blob['query'] + ', ' + blob[field].astype(str)

        return blob

    def request(self, state: str):

        # The state's data URL
        source = self.url.format(state=state)

        # Reading-in
        streams = self.read(source=source)

        # Address NaN str cells
        streams = self.format(blob=streams)

        # Calculate decimal coordinates
        streams = self.getcoordinates(blob=streams)

        # Query
        computations = self.getquery(blob=streams)

        # Compute
        data = computations.compute()
        data = data.groupby(by='TRIFID').first().reset_index(drop=False)

        return data, computations
