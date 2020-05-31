import geopandas as gpd
import pandas as pd


class GeoPandasCoders:
    """
    Class GoePandasCoders
    """

    def __init__(self):
        """
        The constructor
        """
        self.provider = 'nominatim'
        self.user_agent = 'spatial.analysis'

    def via(self, data: str):
        """
        :param data: An address string whose latitude & longitude coordinates will be searched-for
        :return:
            A pandas.core.series.Series of geopy.Location objects, if the address is
            located, otherwise a None series.
        """

        try:
            return gpd.tools.geocode(data, provider=self.provider, user_agent=self.user_agent).loc[0, :]
        except RuntimeError:
            return pd.Series({'geometry': None, 'address': None})

    def geocoding(self, data: gpd.GeoDataFrame, field: str):

        """
        :param data: A geopandas.GeoDataFrame
        :param field: The field of addresses whose latitude & longitude coordinates will
                      be searched-for
        :return:
            A GeoDataFrame consisting of field, a geometry object, address, latitude,
            and longitude.  If an instance of field is not found a record will not be
            associated.
        """

        instances = data.copy()

        estimates = instances.apply(lambda x: self.via(x[field]), axis=1)
        estimates.dropna(axis=0, how='any', inplace=True)

        instances = instances.join(estimates, how='inner')
        instances['latitude'] = instances.geometry.y
        instances['longitude'] = instances.geometry.x

        return instances
