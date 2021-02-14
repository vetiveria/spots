"""
Module naics: North American Industry Classification System reader
"""
import pandas as pd


class NAICS:
    """
    Ref. https://www2.census.gov/programs-surveys/cbp/technical-documentation/
    reference/naics-descriptions/naics2017.txt

    In progress
    """

    def __init__(self):
        """
        Constructor
        """
        self.dataurl = 'https://raw.githubusercontent.com/vetiveria/spots/develop/' \
                       'resources/references/naics2017.csv'

    def read(self) -> pd.DataFrame:
        return pd.read_csv(self.dataurl, header=0, sep=',', encoding='UTF-8')

    @staticmethod
    def convert(naics) -> pd.DataFrame:
        """
        Convert the NAICS codes to integers; 'all sectors' is set to 0

        :param naics: DataFrame
        :return:
        """

        naics['NAICS'] = naics.NAICS.str.strip('-').str.strip('/').str.strip()
        naics['NAICS'] = pd.to_numeric(naics.NAICS, errors='coerce').fillna(0).astype(int)
        naics.rename(columns={'NAICS': 'naics', 'DESCRIPTION': 'description'}, inplace=True)

        return naics

    def exc(self):
        """
        Entry point

        :return:
        """
        naics = self.read()
        naics = self.convert(naics=naics)

        return naics
