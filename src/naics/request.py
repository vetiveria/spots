import os

import dask
import dask.dataframe as dd

import src.naics.api
import src.naics.settings


class Request:

    def __init__(self):
        settings = src.naics.settings.Settings()

        settings.directories()

        self.fields, self.names, self.kwargs = settings.getattributes()

        self.sector = settings.sector
        self.subsector = settings.subsector
        self.group = settings.group

        self.path = settings.path

    def read(self, urlstrings):

        try:
            streams = dd.read_csv(urlpath=urlstrings, blocksize=None, **self.kwargs)
        except OSError as err:
            raise ("OS Error: {0}".format(err))

        # Initially, the data does not have a header row
        streams = streams.rename(columns=self.names)

        return streams

    @staticmethod
    def feed(state: str):
        api = src.naics.api.API()
        return api.url().format(state=state)

    def features(self, data):

        data['NAICS_SECTOR'] = data.NAICS_CODE.astype(str).str.slice(self.sector.start, self.sector.end)
        data['NAICS_SUBSECTOR'] = data.NAICS_CODE.astype(str).str.slice(self.subsector.start, self.subsector.end)
        data['NAICS_GROUP'] = data.NAICS_CODE.astype(str).str.slice(self.group.start, self.group.end)

        return data

    def exc(self, states: list):

        # The URL strings
        sources = [dask.delayed(self.feed)(state) for state in states]
        urlstrings = dask.compute(sources, scheduler='processes')[0]

        # The data
        data = self.read(urlstrings=urlstrings)

        # Features
        data = self.features(data=data)
        data.visualize(filename='naics', format='pdf')

        # Write
        # https://docs.dask.org/en/latest/dataframe-api.html#dask.dataframe.DataFrame.to_csv
        kwargs = {'index': False, 'header': True, 'encoding': 'UTF-8'}
        names = [os.path.join(self.path, state + '.csv') for state in states]
        data.to_csv(names, **kwargs)
