import os

import geopandas as gpd
import pandas as pd

import src.io.files as files


class Shapes:

    def __init__(self):
        """
        The Constructor
        """

    @staticmethod
    def files(blob, path):
        files.Files.cleanup(path=path)
        files.Files.directories(path=path)
        files.Files.extract(blob=blob, path=path)

    @staticmethod
    def filepath(path: str, filestring: str):

        # Determine path components
        sections = [directory for _, directories, _ in os.walk(path, topdown=True)
                    for directory in directories]

        if len(sections) == 0:
            base_directory = ''
        else:
            base_directory = sections[0]

        return os.path.join(path, base_directory, filestring)

    @staticmethod
    def inspect(func):

        try:
            data = func
        except OSError as err:
            print("OS Error: {0}".format(err))
            raise

        return data

    def read(self, filepath: str, ext: str):

        # Retrieve data from a file of interest
        if ext == 'shp':
            data = self.inspect(gpd.read_file(filename=filepath))
        elif ext == 'csv':
            data = self.inspect(pd.read_csv(filepath_or_buffer=filepath))
        else:
            raise ()

        return data

    def request(self, blob, path, ext, filestring):
        """
        :params blob: The URL of the archived file
        :params path: The directory into which files are extracted
        :params ext: The extension of a file of interest - this ensures that the data is
                     read-in via an appropriate method
        :params filestring: The name of the file, including its extension, to be read-in
        """

        # Download the data files
        self.files(blob, path)

        # The local filepath string to the file of interest
        filepath = self.filepath(path, filestring)

        # Data
        return self.read(filepath=filepath, ext=ext)
