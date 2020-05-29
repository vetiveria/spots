import pandas as pd


class Settings:

    def __init__(self):

        self.ofinterest = ['TRIFID', 'LATITUDE', 'LONGITUDE', 'COUNTYGEOID', 'FACILITY_NAME', 'STREET',
                           'CITY',  'STUSPS', 'ZIP_CODE', 'FAC_CLOSED_IND', 'ASGN_FEDERAL_IND', 'BIA_CODE',  'query']

    @staticmethod
    def attributes() -> pd.DataFrame:

        urlstring = 'https://raw.githubusercontent.com/greyhypotheses/hub/develop/' \
                    'data/countries/us/environment/toxins/facilitiesServices.csv'
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

        return fields, names, types

    def getstringfields(self) -> list:

        attributes = self.attributes()
        fields = attributes.loc[attributes.type == 'str', 'rename'].to_list()

        return fields
