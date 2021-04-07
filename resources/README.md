## [for spots](https://github.com/vetiveria/spots)

Data dictionaries and references for the repository [spots](https://github.com/vetiveria/spots)

<br>

### The Toxics Release Inventory (TRI) Data Sets

Due to the incomplete nature of the facilities data 
of [TRI Web Services](https://www.epa.gov/enviro/tri-reported-chemical-information-subject-area-model), facilities 
data is collated via two sources:

##### Via TRI Explorer

URL

* https://enviro.epa.gov/triexplorer/tri_release.facility

Fields read

* [attributes.csv](tri/explorer/attributes.csv)

<br>

##### Via TRI Web Services

Using the TRI_FACILITY data of [TRI Model](https://www.epa.gov/enviro/tri-reported-chemical-information-subject-area-model), i.e.,

* https://data.epa.gov/efservice/TRI_FACILITY

Fields read

* [attributes.csv](tri/services/attributes.csv)

<br>
<br>

### Releases

For toxins release data obtained via the tables of

* https://www.epa.gov/enviro/tri-reported-chemical-information-subject-area-model

Fields of interest

* [releases](releases/releases.csv)

<br>
<br>

### NAICS Data

Obtained via TR_FACILITY & TRI_SUBMISSION_NAICS of

* https://www.epa.gov/enviro/tri-reported-chemical-information-subject-area-model

Fields of interest

* [naics](naics/naics.csv)

References:

* https://www.census.gov/programs-surveys/cbp/technical-documentation/reference/naics-descriptions.html
* https://www.census.gov/programs-surveys/economic-census/guidance/understanding-naics.html
* naics: https://www2.census.gov/programs-surveys/cbp/technical-documentation/reference/naics-descriptions/

<br>
<br>

### Industries

Data Source:

* industry code: https://enviro.epa.gov/enviro/EF_METADATA_HTML.tri_page?p_column_name=INDUSTRY_CODE

<br>
<br>

### Chemicals

* [Envirofacts Data Service API for TRI_CHEM_INFO](https://enviro.epa.gov/enviro/ef_metadata_html.ef_metadata_table?p_table_name=tri_chem_info&p_topic=tri)
* [TRI Reported Chemical Information Subject Area Model](https://www.epa.gov/enviro/tri-reported-chemical-information-subject-area-model)

<br>
<br>


