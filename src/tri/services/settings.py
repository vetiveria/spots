import dask.dataframe as dd
import pandas as pd


class Settings:

    def __init__(self):

        self.name = 'Settings'

    @staticmethod
    def attributes() -> pd.DataFrame:
        """
        Reads-in a set of data set attributes w.r.t. the data source TRI Services

        :return:
            DataFrame of attributes
        """

        # URL of attributes file ... switch to local
        urlstring = 'https://raw.githubusercontent.com/premodelling/dictionaries/develop/spots/' \
                    'src/tri/services/attributes.csv'

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

    def getstringfields(self) -> list:

        attributes = self.attributes()
        fields = attributes.loc[attributes.type == 'str', 'rename'].to_list()

        return fields

    def format(self, blob: dd.DataFrame):

        data = blob.copy()
        for field in self.getstringfields():
            data[field] = data[field].str.strip().fillna(value='')

        data['ZIP_CODE'] = data['ZIP_CODE'].replace(to_replace='[^0-9]', value='', regex=True)
        data['ZIP_CODE'] = data['ZIP_CODE'].replace(to_replace='', value='0', regex=False)
        data['ZIP_CODE'] = dd.to_numeric(arg=data.ZIP_CODE, errors='coerce')

        return data
