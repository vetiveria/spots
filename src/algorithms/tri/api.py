class API:
    """
    A class that builds the URL string of the old TRI data source.  Beware of the URL arguments

        state: The state federal information processing numeric code, i.e.,
               ISO 3166-2:US, e.g., Louisiana -> 22.

        county: GEOID, which is a concatenation of ISO 3166-2:US & county
                code, e.g., 22095 for St. John the Baptist (095) in Louisiana (22).  Or All+counties

        year
    """

    def __init__(self):
        self.name = ''

    @staticmethod
    def root():
        database = 'release_fac'
        return f'https://enviro.epa.gov/triexplorer/{database}'

    @staticmethod
    def affix() -> str:
        """
        Encodes the non-standard API parameter strings
        :return:
        """
        argument = 'fld=TRIID&fld=LNGLAT'
        return '?{}'.format(argument)

    @staticmethod
    def parameters() -> dict:
        p_view = 'STFA'
        trilib = 'TRIQ1'
        sort = '_VIEW_'
        sort_fmt = '1'
        state = '{state}'
        county = r'All+counties'
        chemical = r'All+chemicals'
        industry = 'ALL'
        year = '{year}'
        tab_rpt = '1'
        poutput = 'csv'

        return {'p_view': p_view, 'trilib': trilib, 'sort': sort, 'sort_fmt': sort_fmt, 'state': state,
                'county': county, 'chemical': chemical, 'industry': industry, 'year': year, 'tab_rpt': tab_rpt,
                'poutput': poutput}

    def url(self):
        parameters = self.parameters()
        affix = self.affix()

        for k, v in parameters.items():
            setup = '='.join([k, v])
            affix = '&'.join([affix, setup])

        return self.root() + affix
