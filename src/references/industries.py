"""
Module industries: United States Environmental Protection Agency industry codes
"""
import pandas as pd


class Industries:
    """
    ref. https://enviro.epa.gov/enviro/EF_METADATA_HTML.tri_page?p_column_name=INDUSTRY_CODE

    In progress
    """

    def __init__(self):

        self.dataurl = 'https://raw.githubusercontent.com/discourses/hub/develop/data/' \
                           'countries/us/industries/industrycode.csv'

    def read(self):

        try:
            industries = pd.read_csv(self.dataurl, header=0, sep=',', encoding='UTF-8')
        except OSError as err:
            raise err

        industries.rename(columns={'Industry Code': 'industry_code', 'Industry Name': 'name'}, inplace=True)

        return industries
