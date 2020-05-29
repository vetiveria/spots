
class API:

    def __init__(self):
        self.name = ''

    @staticmethod
    def root():
        database = 'efservice'
        return f'https://data.epa.gov/{database}/'

    @staticmethod
    def parameters():
        return 'TRI_FACILITY/STATE_ABBR/{state}/CSV'

    def url(self):
        return self.root() + self.parameters()
