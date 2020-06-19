import math

import dask.dataframe as dd
import numpy as np

import src.tri.services.api
import src.tri.services.settings
import src.functions.geodetic


class Request:

    def __init__(self):
        """
        The constructor
        """

        api = src.tri.services.api.API()
        self.url = api.url()

        self.settings = src.tri.services.settings.Settings()
        self.fields, self.names, self.kwargs = self.settings.getattributes()

    def read(self, source):
        """
        Reads an online CSV file
        :param source: The URL to a CSV source
        :return:
        """

        try:
            data = dd.read_csv(urlpath=source, blocksize=32000000, **self.kwargs)
        except OSError as err:
            raise ('OS Error {0}'.format(err))

        return data.rename(columns=self.names)

    @staticmethod
    def getcoordinates(blob: dd.DataFrame):
        """
        ... by converting the degree/minute/second geodetic values to decimal geodetic values

        :param blob: The DataFrame whereby decimal geodetic values will be calculated per
                     record, wherever possible

        :return:
        """

        data = blob.copy()
        geodetic = src.functions.geodetic.Geodetic()

        data['LATITUDE'] = data['FAC_LATITUDE'].apply(
            lambda x: geodetic.geodetic(measure=x) if not math.isnan(x) else np.nan,
            meta=('FAC_LATITUDE', 'float64'))

        data['LONGITUDE'] = data['FAC_LONGITUDE'].apply(
            lambda x: geodetic.geodetic(measure=x, direction=-1) if not math.isnan(x) else np.nan,
            meta=('FAC_LONGITUDE', 'float64'))

        return data.drop(columns=['FAC_LATITUDE', 'FAC_LONGITUDE'])

    @staticmethod
    def getquery(blob: dd.DataFrame):
        """
        Creates the an address query per record

        :param blob: The DataFrame whose address query field is being created via
                     the fields FACILITY_NAME, STREET, CITY, STUSPS, ZIP_CODE

        :return:
        """

        blob['query'] = blob.FACILITY_NAME + ' ' + blob.STREET
        for field in ['CITY', 'STUSPS', 'ZIP_CODE']:
            blob['query'] = blob['query'] + ', ' + blob[field].astype(str)

        return blob

    def exc(self, state: str):
        """
        Gets the facilities data of a state

        :param state: The STUSPS, i.e., the 2 letter code, of a state.

        :return: DataFrame, Dask Computations Outline
        """

        # The state's data URL
        source = self.url.format(state=state)

        # Reading-in
        streams = self.read(source=source)

        # Address NaN str cells
        streams = self.settings.format(blob=streams)

        # Calculate decimal coordinates
        streams = self.getcoordinates(blob=streams)

        # Query
        computations = self.getquery(blob=streams)

        # Compute
        data = computations.compute()
        data = data.groupby(by='TRIFID').first().reset_index(drop=False)

        return data, computations
