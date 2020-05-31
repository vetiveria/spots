import pandas as pd

import requests


class Settings:

    def __init__(self):

        # The years for which data exists
        self.starting = 1988
        self.ending = 2018
        self.years = range(self.starting, self.ending + 1)



        # The TRIFID code pattern
        self.pattern = '^([0-9]{3,5}[^AEIOU]{4,5}[A-Z0-9]{4,6})'

    @staticmethod
    def source():

        # URL of attributes file
        urlstring = 'https://raw.githubusercontent.com/greyhypotheses/hub/develop/' \
                    'data/countries/us/environment/toxins/facilities.csv'

        # Read-in
        try:
            names = pd.read_csv(urlstring, header=0, encoding='UTF-8')
        except OSError as err:
            raise ("OS Error: {0}".format(err))

        # Types
        types = {0: 'str', 1: 'str', 2: 'str',
                      3: 'str', 4:  'str', 5: 'str'}

        # Hence
        fields = names.field.to_dict()
        indices = list(range(0, len(fields)))
        kwargs = {'usecols': indices, 'header': None, 'skiprows': 5,
                  'encoding': 'UTF-8', 'dtype': types,
                  'skipinitialspace': True, 'error_bad_lines': True, 'warn_bad_lines': True}

        return fields, kwargs

    @staticmethod
    def hasdata(dataurl: str) -> bool:

        try:
            req = requests.get(dataurl)
        except OSError as err:
            raise Exception(err)

        query = req.text.title().strip().replace('"', '')

        return not query.lower().startswith('no data for tri release')
