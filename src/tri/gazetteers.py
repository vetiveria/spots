import os

import src.functions.mapping
import src.tri.settings


class Gazetteers:

    def __init__(self, crs, latest):
        self.crs = crs
        self.latest = latest

        settings = src.tri.settings.Settings()
        settings.directories()

        self.ofinterest = settings.ofinterest
        self.mapablepath = settings.mapablepath
        self.unmapablepath = settings.unmapablepath

        self.mapping = src.functions.mapping.Mapping(crs=self.crs)

    def gettracts(self, mapable, tracts):

        # Determine the tract that each site belongs to
        maps = self.mapping.within(blob=self.mapping.frame(blob=mapable),
                                   references=tracts.drop(columns=['COUNTYGEOID']))
        maps = maps[self.ofinterest]

        return maps

    def exc(self, mapable, unmapable, tracts, stusps):

        maps = self.gettracts(mapable=mapable, tracts=tracts)

        # Save maps
        maps.to_csv(path_or_buf=os.path.join(self.mapablepath, stusps + '.csv'), index=False, encoding='UTF-8')

        # Save unmapable
        if not unmapable.empty:
            unmapable.to_csv(path_or_buf=os.path.join(self.unmapablepath, stusps + '.csv'), index=False,
                             encoding='UTF-8')
