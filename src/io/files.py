import io
import os
import zipfile

import requests


class Files:

    @staticmethod
    def extract(blob: str, path: str):
        """
        :param blob: A Zip archive's URL
        :param path: The local target directory of the extracts
        """

        try:
            req = requests.get(blob)
        except OSError as err:
            print(err)
            raise

        zipped_object = zipfile.ZipFile(io.BytesIO(req.content))
        zipped_object.extractall(path=path)

    @staticmethod
    def cleanup(path: str):
        """

        :param path: directory path
        :return:
        """

        [os.remove(os.path.join(base, file))
         for base, directories, files in os.walk(path)
         for file in files]

        [os.removedirs(os.path.join(base, directory))
         for base, directories, files in os.walk(path, topdown=False)
         for directory in directories
         if os.path.exists(os.path.join(base, directory))]

    @staticmethod
    def directories(path: str):
        """
        :param path: The local target directory of the extracts
        """

        if not os.path.exists(path=path):
            os.mkdir(path=path)
