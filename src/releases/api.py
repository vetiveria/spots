"""
Module api
"""


class API:
    """
    The API of the hazards releases data
    """

    def __init__(self):
        """
        Constructor
        """
        self.name = ''

    @staticmethod
    def root():
        """
        Root URL

        :return:
        """
        database = 'efservice'
        return f'https://data.epa.gov/{database}/'

    @staticmethod
    def parameters():
        """
        Parameter settings of interest

        :return:
        """
        return '/TRI_FACILITY/STATE_ABBR/{state}/TRI_REPORTING_FORM/REPORTING_YEAR/{year}/TRI_RELEASE_QTY/CSV'

    def url(self):
        """
        URL

        :return:
        """
        return self.root() + self.parameters()
