import dask.dataframe as dd
import numpy as np
import pandas as pd
import requests


class Settings:

    def __init__(self):
        """
        The constructor
        """

        # The years for which data exists
        self.starting = 1988
        self.ending = 2018
        self.years = range(self.starting, self.ending + 1)

        # The TRIFID code pattern
        self.pattern = '^([0-9]{3,5}[^AEIOU]{4,5}[A-Z0-9]{4,6})'

    @staticmethod
    def attributes() -> pd.DataFrame:
        """
        Reads-in a set of data set attributes w.r.t. the data source TRI Explorer

        :return:
            DataFrame of attributes
        """

        # URL of attributes file ... switch to local
        urlstring = 'https://raw.githubusercontent.com/premodelling/dictionaries/develop/spots/' \
                    'src/tri/explorer/attributes.csv'

        # Read-in
        try:
            data = pd.read_csv(urlstring, header=0, encoding='UTF-8')
        except OSError as err:
            raise ("OS Error: {0}".format(err))

        return data

    def getattributes(self):

        # Data reading attributes for TRI Explorer
        attributes = self.attributes()

        # Hence
        fields = attributes.field.to_dict()
        types = attributes.type.to_dict()
        indices = list(range(0, len(fields)))
        kwargs = {'usecols': indices, 'header': None, 'skiprows': 5, 'encoding': 'UTF-8', 'dtype': types,
                  'skipinitialspace': True, 'error_bad_lines': True, 'warn_bad_lines': True}

        return fields, kwargs

    @staticmethod
    def hasdata(dataurl: str) -> bool:
        """
        Does data exist at 'dataurl'?

        :param dataurl: The URL whose data state is being determined

        :return:
        """

        try:
            req = requests.get(dataurl)
        except OSError as err:
            raise Exception(err)
        query = req.text.title().strip().replace('"', '')

        return not query.lower().startswith('no data for tri release')

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
