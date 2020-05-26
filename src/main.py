import src.algorithms.tri.settings
import src.algorithms.tri.api


def main():

    settings = src.algorithms.tri.settings.Settings()
    api = src.algorithms.tri.api.API()

    print(settings.crs)
    print(api.url())


if __name__ == '__main__':
    main()
