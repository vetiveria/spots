import os
import sys


def main():

    settings = src.settings.Settings()

    # TRI Sources
    explorer = src.tri.explorer.request.Request()
    services = src.tri.services.request.Request()

    # Intersection? Union?
    intersections = src.tri.intersections.Intersections()

    # Instantiate an instance of boundaries, and get states data
    boundaries = src.boundaries.boundaries.Boundaries(crs=settings.crs)
    states = boundaries.states(year=settings.latest)

    # The gazetteers
    gazetteers = src.tri.gazetteers.Gazetteers(crs=settings.crs, latest=settings.latest)

    # Get the hazardous spots data per state
    for i in states.index:
        # Get the TRI facilities data of a state via (a) the old TRI repository, and (b) web services
        # Each depends on Dask
        data, computations = explorer.exc(state=states.GEOID[i])
        rdata, rcomputations = services.exc(state=states.STUSPS[i])

        # Merge
        both = data.merge(rdata, how='outer', on='TRIFID')
        mapable, unmapable = intersections.request(blob=both, state=states.GEOID[i])

        # Get the tracts data of a state
        tracts = boundaries.tracts(state=states.GEOID[i], year=settings.latest)
        tracts.rename(columns={'GEOID': 'TRACTGEOID'}, inplace=True)

        # Map
        gazetteers.exc(mapable, unmapable, tracts, states.STUSPS[i])

        # Temporary
        computations.visualize(filename='computations', format='pdf')
        rcomputations.visualize(filename='rcomputations', format='pdf')

        del tracts


if __name__ == '__main__':
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    import src.boundaries.boundaries

    import src.tri.explorer.request
    import src.tri.services.request
    import src.tri.intersections
    import src.tri.gazetteers

    import src.settings

    main()
