import os
import sys


def main():

    # Package level settings
    settings = src.settings.Settings()

    # Instantiate an instance of boundaries, and get states data
    boundaries = src.boundaries.boundaries.Boundaries(crs=settings.crs)
    states = boundaries.states(year=settings.latest)

    # Get the NAICS data
    request = src.naics.request.Request()
    request.exc(states.STUSPS.to_list())


if __name__ == '__main__':
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    import src.boundaries.boundaries
    import src.naics.api
    import src.naics.request
    import src.settings

    main()
