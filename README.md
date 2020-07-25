About industries and toxins.  These notes are updated continuously.  Thus far, the data measures w.r.t. the tri, naics, and releases packages are

package | measurements
 --- | ---
 src/tri | [spots](https://github.com/perennials/measurements/tree/master/src/spots)
 src/naics | [naics](https://github.com/perennials/measurements/tree/master/src/naics)
 src/releases | [designs](https://github.com/perennials/measurements/tree/master/src/designs)

<br>
<br>

* [Python Enviroment](#python-environment)
  * [Anaconda](#anaconda)
  * [VENV](#venv)
  * [Conventions](#conventions)
* [Operating Systems Peculiarities](#operating-systems-peculiarities)
  * [Bash](#bash)
* [Decimals](#decimals)
* [Chemicals](#chemicals)
* [References](#references)

<br>
<br>

### Python Environment

In preparation for Docker, etc.

#### Anaconda

The suggestions of geopandas, https://geopandas.org/install.html, fail

```bash
    conda create --prefix ...environment
    conda activate environment

    conda config --env --add channels conda-forge
    conda config --env --set channel_priority strict
    conda install python=3.7 geopandas
```

Instead

```bash
  conda create --prefix ...environment
  conda activate environment

  conda install -c anaconda python=3.7.7 geopandas nodejs jupyterlab
                   pywin32 pytest coverage pytest-cov pylint pyyaml    
```

And geopy ... Next time set-up

```bash
  conda config --env --add channels anaconda
  conda config --env --set channel_priority strict
```

In relation to requirements.txt

````markdown
    pip freeze -r docs/filter.txt > requirements.txt
````

The file [filter.txt](./docs/filter.txt) summarises the directly installed packages.  Hence, [filter.txt](./docs/filter.txt) is used to create a demarcated [requirements.txt](requirements.txt).  Note:

* scikit-learn is included for **releases** analysis purposes.  It is not used by `spots`, but it is used by `analysis.ipynb` (Google Colaboratory).
* The above applies to `matplotlib` & `seaborn`
* `nodejs` cannot be included in `filter.txt`

<br>

#### VENV

An option, ``virtual env`` instead of ``conda``; details w.r.t. [virtual env](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).  Ensure that the pip version is ≥ 20.0.2.  Also required: [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

```bash
python -m venv env
env\Scripts\activate.bat
python -m pip install --upgrade pip==20.1.1
pip install numpy
```

<br>

Prior to installing [geopandas via pip](https://geopandas.org/install.html#installing-with-pip) ``numpy`` must be installed, and a set of [wheels](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyproj) are required; shapely, fiona, pyproj, and rtree.  Use the command `pip install env\Scripts\{...}.whl` to install wheel files; the command assumes that the .whl files in question are hosted by env\Scripts\.

<br>

#### Conventions

* pylint --generate-rcfile > .pylintrc


<br>
<br>


### Operating Systems Peculiarities

#### Bash

Beware of bash files created within a Windows environment.  The conversion

```bash
  dos2unix.exe *.sh
```

might be required.

<br>
<br>

### Decimals

This exercise is about hazardous waste in the states and territories of the U.S.A.  The locations of these facilities are encoded by the `fac_latitude` & `fac_longitude` fields.  However, a number of facilities do not have `fac_latitude` & `fac_longitude` values.  Hence, the latitude & longitude values of such facilities will be determined via `geopy`.  The decimal latitude & longitude values of

* https://enviro.epa.gov/enviro/EF_METADATA_HTML.tri_page?p_column_name=FAC_LATITUDE

* https://enviro.epa.gov/enviro/EF_METADATA_HTML.tri_page?p_column_name=FAC_LONGITUDE

are determined via the formula

* decimal form  $= \large{DD} + \frac{MM}{60} + \frac{SS}{3600}$

which converts DDMMSS coordinates to decimal form; note that each fac_latitude/fac_longitude is of the form DDMMSS.

<br>
<br>

### Chemicals

**Important**: The toxins releases data encoded by [TRI_RELEASE_QTY](https://enviro.epa.gov/enviro/ef_metadata_html.ef_metadata_table?p_table_name=tri_release_qty&p_topic=tri) are the **total on-site disposal or other releases** data values.  In a nutshell, it is comparable with the on-site totals w.r.t. [EPA TRI Explorer Release Facility](https://enviro.epa.gov/triexplorer/tri_release.facility).  For example the

* 'Total On-site Disposal or Other Releases' field of [St. John Baptist Parish (2018)](https://enviro.epa.gov/triexplorer/release_fac?p_view=COFA&trilib=TRIQ1&sort=_VIEW_&sort_fmt=1&state=22&county=22095&chemical=All+chemicals&industry=ALL&year=2018&tab_rpt=1&fld=TRIID&fld=LNGLAT&fld=RELLBY&fld=TSFDSP)

wherein

* state = 22
* county = 22095
* year = 2018

is equivalent to the totals per (REPORTING_YEAR, TRI_FACILITY_ID, TRI_CHEM_ID) of

* [tri_facility, tri_reporting_form, tri_release_qty model](https://data.epa.gov/efservice/TRI_FACILITY/STATE_ABBR/LA/STATE_COUNTY_FIPS_CODE/22095/TRI_REPORTING_FORM/REPORTING_YEAR/2018/TRI_RELEASE_QTY/CSV)

built via model

* https://www.epa.gov/enviro/tri-reported-chemical-information-subject-area-model

<br>
<br>

### References

JupyterLab:
* https://jupyterlab.readthedocs.io/en/stable/index.html
* https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html

Anaconda:
* https://docs.anaconda.com/anaconda/install/silent-mode/
* https://docs.anaconda.com/anaconda-adam/install/cloud/#installing-adam

IDE:
* https://www.jetbrains.com/idea/download/other.html

Linux:
* https://www.tecmint.com/18-tar-command-examples-in-linux/
