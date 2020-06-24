## Spots

Probable Toxics Release (TR) spots.  These notes are updates continuously ...

<br>


### Python Enviroment

In preparation for Docker, etc.

##### Anaconda

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

  conda install -c anaconda python=3.7.7 geopandas geopy nodejs jupyterlab
                   pywin32 pytest coverage pytest-cov pylint pyyaml    
```

Next time set-up

```bash
  conda config --env --add channels anaconda
  conda config --env --set channel_priority strict
```

<br>

##### VENV

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

##### The Requirements

````markdown
    pip freeze -r docs/filter.txt > requirements.txt
````

The file [filter.txt](./docs/filter.txt) summarises the directly installed packages.  Hence, [filter.txt](./docs/filter.txt) is used to create a demarcated [requirements.txt](requirements.txt)


<br>
<br>


### Operating Systems Peculiarities

##### Bash

Beware of bash files created within a Windows environment.  The conversion

```bash
  dos2unix.exe *.sh
```

might be required.


<br>
<br>


### Standards

* pylint --generate-rcfile > .pylintrc


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

* https://www.epa.gov/enviro/tri-reported-chemical-information-subject-area-model

<br>
<br>

### Misc

* https://jupyterlab.readthedocs.io/en/stable/index.html
* https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html

* https://docs.anaconda.com/anaconda/install/silent-mode/
* https://docs.anaconda.com/anaconda-adam/install/cloud/#installing-adam

* https://www.jetbrains.com/idea/download/other.html

* https://www.tecmint.com/18-tar-command-examples-in-linux/
