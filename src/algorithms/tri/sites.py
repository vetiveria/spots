import dask
import dask.dataframe
import numpy as np

import src.algorithms.tri.api as api
import src.algorithms.tri.settings as settings


class Sites:

    def __init__(self):
        setup = settings.Settings()

        self.pattern = setup.pattern
        self.years = setup.years
        self.fields = setup.fields()
        self.indices = list(range(0, len(self.fields)))

        self.url = api.API().url()

        self.kwargs = {'usecols': self.indices, 'header': None, 'skiprows': 5, 'encoding': 'UTF-8',
                       'skipinitialspace': True, 'error_bad_lines': True, 'warn_bad_lines': True}

    def reading(self, sources):
        """
        Note, in this case pandas is instructed to drop 'bad lines'
        :params source: The URL of the data
        """

        try:
            streams = dask.dataframe.read_csv(urlpath=sources, blocksize=None, **self.kwargs)
        except OSError as err:
            raise ("OS Error: {0}".format(err))

        # Initially, the data does not have a header row
        streams = streams.rename(columns=self.fields)

        # For 'TRIFID', this (a) removes leading & trailing spaces, and subsequently (b) replaces
        # empty cells with np.nan
        streams['TRIFID'] = streams['TRIFID'].str.strip().replace(to_replace='', value=np.nan)

        return streams

    def filtering(self, streams):

        # This step will also eliminate cases wherein TRIFID.isna()
        condition = streams.TRIFID.str.slice(start=0, stop=15).str.match(self.pattern)
        literals = condition.apply(lambda x: x if x is True else False, meta=('TRIFID', 'bool'))
        estimates = streams[literals]

        # Of interest
        estimates = estimates.drop(columns=['ROW', 'TOTAL'])

        return estimates.drop_duplicates()

    @staticmethod
    def attributes(blob, state: str):
        for field in ['LATITUDE', 'LONGITUDE']:
            blob[field] = blob[field].astype(dtype='float')

        blob['STATEGEOID'] = state

        return blob

    def feed(self, state: str, year: int):

        source = self.url.format(state=state, year=year)
        if settings.Settings.hasdata(dataurl=source):
            return source

    def requesting(self, state: str):

        # The list of a state's data URL strings
        nodes = [dask.delayed(self.feed)(state, year) for year in list(self.years)]
        sources = dask.compute(nodes, scheduler='processes')[0]

        # Reading-in
        streams = self.reading(sources=sources)

        # Filtering-out anomalies and duplicates
        filterings = self.filtering(streams=streams.copy())

        # Ascertain field attributes
        computations = self.attributes(blob=filterings, state=state)

        # Compute
        data = computations.compute()

        return data, computations
