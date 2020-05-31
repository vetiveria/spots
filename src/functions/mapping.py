import pandas as pd

import geopandas as gpd


class Mapping:

    def __init__(self, crs: str):
        self.crs = crs

    def frame(self, blob: pd.DataFrame):

        # Convert the data frame to a geographic data frame: re-visit
        data = gpd.GeoDataFrame(data=blob,
                                geometry=gpd.points_from_xy(blob.LONGITUDE, blob.LATITUDE),
                                crs=self.crs)

        return data

    @staticmethod
    def within(blob: gpd.GeoDataFrame, references: gpd.GeoDataFrame):

        # Determine the polygon geometry, self.references.geometry, that each
        # data.geometry belongs to
        places = gpd.sjoin(left_df=blob, right_df=references, how='inner', op='within')

        return places
