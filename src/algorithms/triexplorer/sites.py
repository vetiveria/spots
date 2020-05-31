import dask
import dask.dataframe as dd
import numpy as np

import src.algorithms.triexplorer.api as api
import src.algorithms.triexplorer.settings as settings


class Sites:

    def __init__(self):
        """
        The constructor
        """
        setup = settings.Settings()
        self.pattern = setup.pattern
        self.years = setup.years
        self.fields, self.kwargs = setup.source()

        self.url = api.API().url()

    def feed(self, state: str, year: int):

        source = self.url.format(state=state, year=year)
        if settings.Settings.hasdata(dataurl=source):
            return source

    def read(self, sources: list):
        """
        Note, in this case pandas is instructed to drop 'bad lines'

        :param sources: The URL strings of the data
        """

        try:
            streams = dd.read_csv(urlpath=sources, blocksize=None, **self.kwargs)
        except OSError as err:
            raise ("OS Error: {0}".format(err))

        # Initially, the data does not have a header row
        streams = streams.rename(columns=self.fields)

        return streams

    @staticmethod
    def format(blob, state: str):
        """
        :param blob:
            A DataFrame of raw sites data

        :param state:
            The 2 digit state code, in string form.

        :return:
            A DataFrame wherein the fields of interest have been appropriately
            formatted; w.r.t. expected type
        """

        # For 'TRIFID', this (a) removes leading & trailing spaces, and subsequently (b) replaces
        # empty cells with np.nan
        blob['TRIFID'] = blob['TRIFID'].str.strip().replace(to_replace='', value=np.nan)

        # Enforce type float
        for field in ['LATITUDE', 'LONGITUDE']:
            blob[field] = dd.to_numeric(arg=blob[field], errors='coerce')

        # State
        blob['STATEGEOID'] = state

        return blob

    def filter(self, blob):
        """
        Filters-out duplicates, eliminates records that have invalid site identification codes

        :param blob:
            A DataFrame of sites data

        :return:
            Filtered DataFrame
        """

        # This step will also eliminate cases wherein TRIFID.isna()
        condition = blob.TRIFID.str.slice(start=0, stop=15).str.match(self.pattern)
        literals = condition.apply(lambda x: x if x is True else False, meta=('TRIFID', 'bool'))
        estimates = blob[literals]

        # Of interest
        estimates = estimates.drop(columns=['ROW', 'TOTAL'])

        estimates = estimates.groupby(by='TRIFID').first().reset_index(drop=False)

        return estimates

    def request(self, state: str):
        """
        Gets a state's sites

        :param state:
            The 2 digit state code, in string form.

        :return:
            DataFrame of sites data
        """

        # The list of a state's data URL strings
        nodes = [dask.delayed(self.feed)(state, year) for year in list(self.years)]
        sources = dask.compute(nodes, scheduler='processes')[0]

        # Reading-in
        streams = self.read(sources=sources)

        # Ascertain field attributes
        formatted = self.format(blob=streams, state=state)

        # Filtering-out anomalies and duplicates
        computations = self.filter(blob=formatted.copy())

        # Compute
        data = computations.compute()

        # Hence
        return data, computations
