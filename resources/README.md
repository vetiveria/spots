## [for spots](https://github.com/discourses/spots)

Data dictionaries for the repository

* https://github.com/discourses/spots

Note, *discourses* is a [greyhypotheses](https://github.com/greyhypotheses) *GitHub Organization*, and [spots](https://github.com/discourses/spots) is a private repository.

<br>

### The Toxics Release Inventory (TRI) Data Sets


##### Via TRI Explorer

Due to the incomplete nature of the facilities data of [TRI Web Services](https://www.epa.gov/enviro/tri-reported-chemical-information-subject-area-model), facilities data is also garnered via

* https://enviro.epa.gov/triexplorer/tri_release.facility

Fields read

* [attributes.csv](src/tri/explorer/attributes.csv)

<br>

##### Via TRI Web Services

Acquired via the TRI_FACILITY data of [TRI Model](https://www.epa.gov/enviro/tri-reported-chemical-information-subject-area-model), i.e., via

* https://data.epa.gov/efservice/TRI_FACILITY

Fields read

* [attributes.csv](src/tri/services/attributes.csv)

<br>
<br>

### Releases

For toxins release data obtained via the tables of

* https://www.epa.gov/enviro/tri-reported-chemical-information-subject-area-model

Fields of interest

* [releases](src/releases/releases.csv)


<br>
<br>

### NAICS Data

Obtained via TR_FACILITY & TRI_SUBMISSION_NAICS of

* https://www.epa.gov/enviro/tri-reported-chemical-information-subject-area-model

Fields of interest

* [naics](src/naics/naics.csv)
