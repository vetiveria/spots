class Settings:

    def __init__(self):

        # For geographic boundaries
        self.crs = 4269
        self.latest = 2018

        # For releases
        self.starting = 1988
        self.ending = 2018
        self.years = range(self.starting, self.ending + 1)
