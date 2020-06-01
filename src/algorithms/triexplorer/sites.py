import dask
import dask.dataframe as dd

import src.algorithms.triexplorer.api
import src.algorithms.triexplorer.settings


class Sites:

    def __init__(self):
        """
        The constructor
        """
        self.settings = src.algorithms.triexplorer.settings.Settings()
        self.pattern = self.settings.pattern
        self.years = self.settings.years
        self.fields, self.kwargs = self.settings.getattributes()

        api = src.algorithms.triexplorer.api.API()
        self.url = api.url()

    def feed(self, state: str, year: int):
        """
        :param state:
            The 2 digit state code, in string form.

        :param year:
            Data year

        :return:
            A state's data URL, for a given year, if data exists for that year
        """

        source = self.url.format(state=state, year=year)
        if self.settings.hasdata(dataurl=source):
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
        urlstrings = [node for node in nodes if node is not None]
        sources = dask.compute(urlstrings, scheduler='processes')[0]

        # Reading-in
        streams = self.read(sources=sources)

        # Ascertain field attributes
        formatted = self.settings.format(blob=streams, state=state)

        # Filtering-out anomalies and duplicates
        computations = self.filter(blob=formatted.copy())

        # Compute
        data = computations.compute()

        # Hence
        return data, computations
