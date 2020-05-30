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
    def fields():

        urlstring = 'https://raw.githubusercontent.com/greyhypotheses/hub/develop/' \
                    'data/countries/us/environment/toxins/facilities.csv'
        try:
            names = pd.read_csv(urlstring, header=0, encoding='UTF-8')
        except OSError as err:
            raise ("OS Error: {0}".format(err))

        return names.field.to_dict()

    @staticmethod
    def hasdata(dataurl: str) -> bool:

        try:
            req = requests.get(dataurl)
        except OSError as err:
            raise Exception(err)

        query = req.text.title().strip().replace('"', '')

        return not query.lower().startswith('no data for tri release')
