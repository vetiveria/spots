import pandas as pd
import dotmap
import os


class Settings:

    def __init__(self):

        # The industry sector, subsector, & group w.r.t. the NAICS_CODE string
        self.sector, self.subsector, self.group = dotmap.DotMap({'start': 0, 'end': 2}), \
                                                  dotmap.DotMap({'start': 0, 'end': 3}), \
                                                  dotmap.DotMap({'start': 0, 'end': 4})

        # Store the NAICS data in
        self.path = os.path.join('naics')

    def directories(self):

        if not os.path.exists(self.path):
            os.makedirs(self.path)

    @staticmethod
    def attributes() -> pd.DataFrame:

        # Switch to local
        urlstring = 'https://raw.githubusercontent.com/greyhypotheses/dictionaries/develop/spots/src/naics/naics.csv'

        try:
            data = pd.read_csv(urlstring, header=0, encoding='UTF-8')
        except OSError as err:
            raise ("OS Error: {0}".format(err))

        return data

    def getattributes(self) -> (list, dict, dict):

        attributes = self.attributes()

        fields = attributes.field.to_list()
        names = attributes[['field', 'rename']].set_index(keys='field').to_dict(orient='dict')['rename']
        types = attributes[['field', 'type']].set_index(keys='field').to_dict(orient='dict')['type']

        kwargs = {'usecols': fields, 'header': 0, 'encoding': 'UTF-8',
                  'sep': ',', 'dtype': types}

        return fields, names, kwargs
