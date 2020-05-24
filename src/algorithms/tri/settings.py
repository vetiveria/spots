class Settings:

    def __init__(self):
        self.name = 'Settings'

        self.starting = 1988
        self.ending = 2018
        self.years = range(self.starting, self.ending + 1)
        self.latest = self.years[-1]

        self.crs = 4269
