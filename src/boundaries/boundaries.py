import os

import geopandas as gpd

import src.boundaries.shapes


class Boundaries:
    """
    Class Boundaries: Reads the country boundaries of the U.S.A, hence package name 'us'
    """

    def __init__(self, crs):
        """
        The constructor
        :param crs: The required coordinate reference system (CRS),
                    e.g., 4326 (https://epsg.io/4326)
        """
        self.crs = crs
        self.shapes = src.boundaries.shapes.Shapes()

    def coordinates(self, blob: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        """
        Sets the CRS of a GeoDataFrame
        :param blob: The GeoDataFrame whose coordinate system is being set.
        :return: A GeoDataFrame that has the required CRS
        """

        if not blob.crs == self.crs:
            blob.to_crs('epsg:{}'.format(self.crs))

        return blob

    def request(self, blob: str, path: str, ext: str, filestring: str) -> gpd.GeoDataFrame:
        """

        :param blob: The URL of the archived set of files
        :param path: The directory into which files are de-archived
        :param ext: The extension of the file of interest - this ensures that the data is
                    read-in via an appropriate method
        :param filestring: The name of the file, including its extension, to be read-in
        :return:
        """

        outlines = self.shapes.request(blob=blob, path=path, ext=ext, filestring=filestring)
        outlines = self.coordinates(outlines)

        return outlines

    def tracts(self, state: str, year: int):
        """
        Reads census tract shape files.
        :param state: The GEOID of the state of interest.  Pattern -> ^([0-9]{2})
        :param year: The year. Pattern -> YYYY
        :return:
        """

        path = os.path.join('tracts', '{year}'.format(year=year), '{state}'.format(state=state))
        if not os.path.exists(path=path):
            os.makedirs(path)

        base = 'https://www2.census.gov/geo/tiger/GENZ{year}/shp/cb_{year}_{state}_tract_500k.zip'
        blob = base.format(state=state, year=year)
        ext = 'shp'
        filestring = 'cb_{year}_{state}_tract_500k.shp'.format(state=state, year=year)

        data = self.request(blob=blob, path=path, ext=ext, filestring=filestring)

        # The county GEOID field
        data['COUNTYGEOID'] = [''.join([x, y]) for x, y in zip(data.STATEFP, data.COUNTYFP)]

        return data

    def counties(self, year):
        """
        Reads counties shape files.
        :param year: The year. Pattern -> YYYY
        :return:
        """

        path = os.path.join('counties', '{year}'.format(year=year))
        if not os.path.exists(path=path):
            os.makedirs(path)

        blob = 'https://www2.census.gov/geo/tiger/GENZ{year}/shp/cb_{year}_us_county_500k.zip'.format(year=year)
        ext = 'shp'
        filestring = 'cb_{year}_us_county_500k.shp'.format(year=year)

        return self.request(blob=blob, path=path, ext=ext, filestring=filestring)

    def states(self, year):
        """
        Reads states shape files.
        :param year: The year. Pattern -> YYYY
        :return:
        """

        path = os.path.join('states', '{year}'.format(year=year))
        if not os.path.exists(path=path):
            os.makedirs(path)

        blob = 'https://www2.census.gov/geo/tiger/GENZ{year}/shp/cb_{year}_us_state_500k.zip'.format(year=year)
        ext = 'shp'
        filestring = 'cb_{year}_us_state_500k.shp'.format(year=year)

        return self.request(blob=blob, path=path, ext=ext, filestring=filestring)
