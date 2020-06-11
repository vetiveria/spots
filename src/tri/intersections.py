import pandas as pd


class Intersections:

    def __init__(self):
        self.name = ''

    @staticmethod
    def estimate(stream: pd.DataFrame, state: str, indices: pd.core.indexes):
        """

        :param stream: The data set
        :param state: The 2 digit string code of a state
        :param indices: The lines whose values will be estimated
        """

        stream.loc[indices, 'LATITUDE_x'] = stream.loc[indices, 'LATITUDE_x'].combine_first(
            stream.loc[indices, 'LATITUDE_y'])
        stream.loc[indices, 'LONGITUDE_x'] = stream.loc[indices, 'LONGITUDE_x'].combine_first(
            stream.loc[indices, 'LONGITUDE_y'])
        stream.loc[indices, 'STATEGEOID'] = state
        stream.loc[indices, 'FACILITY'] = stream.loc[indices, 'FACILITY'].combine_first(stream.loc[indices, 'query'])

        stream.rename(columns={'LATITUDE_x': 'LATITUDE', 'LONGITUDE_x': 'LONGITUDE'}, inplace=True)
        stream.drop(columns=['LATITUDE_y', 'LONGITUDE_y', 'query'], inplace=True)

        return stream

    @staticmethod
    def outliers(stream: pd.DataFrame):
        return stream.LATITUDE.isna() | stream.LONGITUDE.isna()

    def request(self, blob: pd.DataFrame, state: str):
        """

        :param blob: The data set
        :param state: The 2 digit string code of a state
        :return:
        """

        stream = blob.copy()

        # The lines that require latitude, longitude, etc., estimates
        stream['ESTIMATE'] = stream.FACILITY.isna()
        indices = stream[stream.ESTIMATE].index

        # Estimate
        stream = self.estimate(stream=stream.copy(), state=state, indices=indices)

        # Inestimable
        isoutlier = self.outliers(stream=stream)

        # ... unmapable
        unmapable = stream[isoutlier]

        # ... mapable
        mapable = stream.copy()[~isoutlier]

        # Hence
        return mapable, unmapable
