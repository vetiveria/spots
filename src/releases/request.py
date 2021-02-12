"""
Module request
"""
import dask
import dask.dataframe as dd
import requests

import src.releases.api
import src.releases.settings
import src.settings


class Request:
    """
    Class Request

    Requests releases data, and performs a few data checking/structuring tasks
    """

    def __init__(self):
        """
        Constructor
        """

        api = src.releases.api.API()
        self.url = api.url()

        settings = src.releases.settings.Settings()
        _, self.names, _, self.kwargs = settings.getattributes()

        self.years = src.settings.Settings().years

    def read(self, urlstrings) -> dd.DataFrame:
        """
        Reads-in releases data

        :param urlstrings: The API URL strings of the data to be read

        :return: dask.DataFrame of readings
        """

        try:
            streams = dd.read_csv(urlpath=urlstrings, blocksize=None, **self.kwargs)
        except OSError as err:
            raise ("OS Error: {0}".format(err))

        # Initially, the data does not have a header row
        streams = streams.rename(columns=self.names)

        # Fields that should be dropped in the metadata file, eventually
        streams = streams.drop(axis=1, columns=['FACILITY_NAME', 'EPA_REGISTRY_ID', 'CAS_CHEM_NAME',
                                                'RELEASE_BASIS_EST_CODE'])

        return streams

    def feed(self, state, year) -> str:
        """
        Builds the API URL strings w.r.t. a state & year of interest

        :param state: The state abbreviation, i.e., STUSPS, of a U.S.A. state or territory
        :param year: One of the relevant data years, as outlined in src.settings.Settings().years

        :return: An API URL string
        """

        url = self.url.format(state=state, year=year)

        if requests.get(url=url).status_code == 200:
            urlstring = url
        else:
            urlstring = None

        return urlstring

    def exc(self, state) -> dd.DataFrame:
        """

        :param state: The state abbreviation, i.e., STUSPS, of a U.S.A. state or territory

        :return:
        """

        urlobjects = [dask.delayed(self.feed)(state, year) for year in self.years]
        urlstrings = dask.compute(urlobjects, scheduler='processes')[0]
        urlstrings = [string for string in urlstrings if string is not None]

        streams = self.read(urlstrings=urlstrings)
        streams = streams[streams.TRADE_SECRET_IND == 0]

        streams['ENVIRONMENTAL_MEDIUM'] = streams.ENVIRONMENTAL_MEDIUM.str.strip().str.lower()
        streams = streams.drop_duplicates()

        return streams
