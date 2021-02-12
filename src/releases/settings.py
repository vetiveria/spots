import pandas as pd


class Settings:

    def __init__(self):
        self.name = ''

    @staticmethod
    def attributes() -> pd.DataFrame:

        # Switch to local.  Facility level attributes.
        urlstring = 'https://raw.githubusercontent.com/vetiveria/spots/develop/' \
                    'resources/releases/releases.csv'

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

        return fields, names, types, kwargs
