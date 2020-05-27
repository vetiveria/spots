import dask
import dask.dataframe
import numpy as np
import pandas as pd

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
        estimates = estimates.drop(columns=['row', 'total'])

        return estimates.drop_duplicates()

    @staticmethod
    def attributes(blob: pd.DataFrame, state: str):
        blob['LATITUDE'] = blob.LATITUDE.astype(dtype='float', errors='raise')
        blob['LONGITUDE'] = blob.LONGITUDE.astype(dtype='float', errors='raise')
        blob['STATEGEOID'] = state

        return blob

    def feed(self, state: str, year: int):

        source = self.url.format(state=state, year=year)
        if settings.Settings.hasdata(dataurl=source):
            return source

    def requesting(self, state: str):

        nodes = [dask.delayed(self.feed)(state, year) for year in list(self.years)]
        sources = dask.compute(nodes, scheduler='processes')[0]

        streams = self.reading(sources=sources)
        funnel = self.filtering(streams=streams)
        summary = funnel.compute()

        return self.attributes(blob=summary, state=state), funnel
