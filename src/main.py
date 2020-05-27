import src.algorithms.tri.settings
import src.algorithms.tri.api
import src.boundaries.boundaries


def main():

    settings = src.algorithms.tri.settings.Settings()
    api = src.algorithms.tri.api.API()
    entity = src.boundaries.boundaries.Boundaries(crs=settings.crs)

    print(settings.crs)
    print(api.url())

    states = entity.states(year=2018)
    print(states.head())


if __name__ == '__main__':
    main()
