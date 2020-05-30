
class Settings:

    def __init__(self):

        # The coordinate reference system
        self.crs = 4269

        # For geographic boundaries
        self.latest = 2018

        # The fields of interest
        self.ofinterest = ['TRIFID', 'LONGITUDE', 'LATITUDE',
                           'STATEFP', 'COUNTYFP', 'TRACTCE',
                           'COUNTYGEOID', 'TRACTGEOID',
                           'FACILITY_NAME', 'STREET', 'CITY', 'STUSPS', 'ZIP_CODE', 'FACILITY',
                           'FAC_CLOSED_IND', 'ASGN_FEDERAL_IND', 'BIA_CODE']
