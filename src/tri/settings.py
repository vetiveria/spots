import os


class Settings:

    def __init__(self):

        # The fields of interest
        self.ofinterest = ['TRIFID', 'LONGITUDE', 'LATITUDE', 'ESTIMATE',
                           'STATEFP', 'COUNTYFP', 'TRACTCE',
                           'STATEGEOID', 'COUNTYGEOID', 'TRACTGEOID', 'AFFGEOID',
                           'FACILITY_NAME', 'STREET', 'CITY', 'STUSPS', 'ZIP_CODE', 'FACILITY',
                           'FAC_CLOSED_IND', 'ASGN_FEDERAL_IND', 'BIA_CODE', 'EPA_REGISTRY_ID']

        self.mapablepath = os.path.join('spots', 'mapable')
        self.unmapablepath = os.path.join('spots', 'unmapable')

    def directories(self):

        paths = [self.mapablepath, self.unmapablepath]
        for directory in paths:
            if not os.path.exists(directory):
                os.makedirs(directory)
