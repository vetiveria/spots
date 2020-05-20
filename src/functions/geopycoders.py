import geopandas as gpd
import geopy
import geopy.extra.rate_limiter
import pandas as pd


class GeoPyCoders:

    def __init__(self):
        geolocator = geopy.geocoders.Nominatim(user_agent='geo.analysis')
        self.geocode = geopy.extra.rate_limiter.RateLimiter(geolocator.geocode, min_delay_seconds=3)

    def via(self, data: pd.Series):
        """
        :param data: A series of addresses whose latitude & longitude coordinates will be searched-for
        :return:
            A pandas.core.series.Series of geopy.Location objects .. if the address is
            located, None otherwise
        """

        return data.apply(self.geocode)

    def geocoding(self, data: gpd.GeoDataFrame, field: str):
        """
        :param data: A series of addresses whose latitude & longitude coordinates will be searched-for
        :param field: The field of addresses whose latitude & longitude coordinates will
                      be searched-for
        :return:
            A GeoDataFrame of consisting of field, a locale object, a geometry object, address, latitude,
            and longitude.  If an instance of field is not found a record will not be
            associated.
        """

        instances = data.copy()
        instances['locale'] = self.via(instances[field])
        instances['geometry'] = instances.locale.apply(lambda i: tuple(i.point) if i else None)
        instances['address'] = instances.locale.apply(lambda i: i.address if i else None)
        instances['latitude'] = instances.locale.apply(lambda i: i.latitude if i else None)
        instances['longitude'] = instances.locale.apply(lambda i: i.longitude if i else None)

        return instances
