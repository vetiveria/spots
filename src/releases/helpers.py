"""
Module helpers
"""
import geopandas as gpd
import pandas as pd

import src.functions.measures


class Helpers:
    """
    Class Helpers
    """

    def __init__(self, counties: gpd.GeoDataFrame, chemicals: pd.DataFrame):
        """
        The constructor

        :param counties: The counties of the U.S.A.
        :param chemicals: The hazardous chemicals tracked by the United States Environmental Protection Agency
        """

        self.counties = counties
        self.chemicals = chemicals
        self.measures = src.functions.measures.Measures()

    def reference(self, state) -> pd.DataFrame:
        """

        :param state: The state abbreviation, i.e., STUSPS, of a U.S.A. state or territory
        :return: The distinct combinations of counties & chemicals w.r.t. state
        """

        authorities = self.counties.loc[self.counties.STUSPS == state, 'COUNTYGEOID'].values
        combinations = [[authority, chemical] for authority in authorities for chemical in
                        self.chemicals.TRI_CHEM_ID.values]

        return pd.DataFrame(data=combinations, columns=['COUNTYGEOID', 'TRI_CHEM_ID'])

    def units(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Acquires the unit of measure of each chemical in data

        :param data: A set chemicals data
        :return: An expanded data set
        """
        return data.merge(self.chemicals[['TRI_CHEM_ID', 'UNIT_OF_MEASURE']], how='left', on=['TRI_CHEM_ID'])

    def weights(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Weights calculations

        :param data: A set chemicals data
        :return: A data set wherein the chemical weights have the same unit of measure
        """

        # Determine the records that have a pounds measure, subsequently convert the values to kilograms
        indices = data[data.UNIT_OF_MEASURE == 'pounds'].index
        data.loc[indices, 'RELEASE_KG'] = self.measures.pounds_to_kilograms(data.loc[indices, 'TOTAL_RELEASE'])

        # Deduce the records that have a grams measure, subsequently convert the values to kilograms
        originals = data.index.difference(indices)
        data.loc[originals, 'RELEASE_KG'] = data.loc[originals, 'TOTAL_RELEASE'] / 1000

        # Drop the useless columns
        data.drop(columns=['TOTAL_RELEASE', 'UNIT_OF_MEASURE'], inplace=True)

        return data

    def regressors(self, data: pd.DataFrame, state):
        """
        Builds a state's design matrix chemical weights

        :param data: A set chemicals data
        :param state: The state abbreviation, i.e., STUSPS, of a U.S.A. state or territory
        :return:
        """

        # The distinct combinations of (counties.COUNTYGEOID, chemicals.TRI_CHEM_ID)
        reference = self.reference(state=state)

        # reference 'left join' points: This ensures that each design matrix has the
        # same number of chemical fields
        vector = reference.merge(data, how='left', on=['COUNTYGEOID', 'TRI_CHEM_ID'])

        # The design matrix: The chemicals are the regressors, and each row instance encodes
        # the weights per county of a state
        matrix = vector.pivot(index='COUNTYGEOID', columns='TRI_CHEM_ID', values='RELEASE_KG')
        matrix.fillna(value=0, inplace=True)

        return matrix
