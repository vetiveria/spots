import src.algorithms.tri.api as api
import src.algorithms.tri.settings

settings = src.algorithms.tri.settings.Settings()


def main():
    url = api.API().url()
    print(url)

    print(settings.crs)
    


if __name__ == '__main__':
    main()
