"""
Module chemicals
"""
import pandas as pd


class Chemicals:
    """
    Class Chemicals: Reads-in the list of tracked hazardous chemicals
    """

    def __init__(self):
        """
        Constructor: Outlines the data & metadata URL strings
        """

        self.dataurl = 'https://data.epa.gov/efservice/TRI_CHEM_INFO/CSV'

        self.metadataurl = 'https://raw.githubusercontent.com/vetiveria/spots/develop' \
                           'resources/references/chemicals.csv'

    def attributes(self) -> (list, dict, dict):
        """

        :return: Attributes determined via metadata
        """

        metadata = pd.read_csv(self.metadataurl, header=0, encoding='UTF-8')
        fields = metadata.field.values
        names = metadata[['field', 'rename']].set_index(keys='field').to_dict(orient='dict')['rename']
        types = metadata[['field', 'type']].set_index(keys='field').to_dict(orient='dict')['type']

        return fields, names, types

    def read(self) -> pd.DataFrame:
        """

        :return: DataFrame of chemicals
        """

        fields, names, types = self.attributes()

        try:
            chemicals = pd.read_csv(self.dataurl, header=0, encoding='UTF-8', usecols=fields, dtype=types)
        except OSError as err:
            raise Exception(err)

        chemicals.rename(columns=names, inplace=True)

        return chemicals

    def exc(self) -> pd.DataFrame:
        """

        :return: DataFrame of chemicals, after checks
        """

        chemicals = self.read()

        # Not NaN
        chemicals = chemicals[chemicals.TRI_CHEM_ID.notna()]

        # Not a trade secret
        chemicals['TRI_CHEM_ID'] =  chemicals.TRI_CHEM_ID.str.strip().str.upper()
        chemicals = chemicals[chemicals.TRI_CHEM_ID.str.upper() != 'TRD SECRT']

        # Consistent unit of measure values
        chemicals['UNIT_OF_MEASURE'] = chemicals.UNIT_OF_MEASURE.str.strip().str.lower()

        return chemicals
