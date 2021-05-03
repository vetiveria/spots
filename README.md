About industries and toxins.  These notes are updated continuously.  Thus far, the data measures w.r.t. the tri, naics, and releases packages are


* [The Data](#the-data)
  * [Releases](#releases)
  * [Geography & Decimals](#geography--decimals)
* [Development Environment](#development-environment)
  * [Anaconda](#anaconda)
  * [Requirements](#requirements)
  * [Conventions](#conventions)
* [References](#references)
* [Operating Systems Peculiarities](#operating-systems-peculiarities)


<br>
<br>


### The Data

* data.ipynb <br> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vetiveria/spots/blob/develop/data.ipynb)

package |data |comment
:--- |:--- |:---
src/releases | [warehouse/designs](./warehouse/designs) | At present, each release value herein is the total amount of a toxin that has been released thus far in a county.
src/tri | [warehouse/tri](./warehouse/tri) | Each facility's details, e.g., facility unique identifier, latitude, longitude, etc., per state.
src/naics | [warehouse/naics](./warehouse/naics) | Each facility's set of industry classifications per state.
src/references | [warehouse/references](./warehouse/references/naics.csv) | The reference sheet of the NAICS unique identifiers; ref. [north american industry classification codes](https://www.census.gov/naics/).
 | [warehouse/references](./warehouse/references/industries.csv) | The reference sheet of EPA's idustry sectors; ref. [industry sectors & codes](https://www.epa.gov/toxics-release-inventory-tri-program/tri-covered-industry-sectors) of the [toxics release inventory program](https://www.epa.gov/toxics-release-inventory-tri-program)
 | ... | chemical names

<br>
<br>


### Development Environment

In preparation for Docker, etc.

#### Anaconda

Altogether

```bash
  conda create --prefix ...environment
  conda activate environment

  conda install -c anaconda python=3.7.7 geopandas nodejs jupyterlab
                   pywin32 pytest coverage pytest-cov pylint pyyaml
                   
  conda install -c anaconda python-graphviz   
  
  conda install -c anaconda xlrd
```

And for geopy, quantities, and dotmap

```bash
  pip install ...    
```

Next time set-up

```bash
  conda config --env --add channels anaconda
  conda config --env --set channel_priority strict
```

<br>

**failures**

The suggestions of geopandas, https://geopandas.org/install.html, fail

```bash
    conda create --prefix ...environment
    conda activate environment

    conda config --env --add channels conda-forge
    conda config --env --set channel_priority strict
    conda install python=3.7 geopandas
```

<br>

**venv**

A development environment option is ``virtual env`` instead of ``conda``; details w.r.t. [virtual env](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).  Ensure that the pip version is ≥ 20.0.2.  Also required: [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

```bash
python -m venv env
env\Scripts\activate.bat
python -m pip install --upgrade pip==20.1.1
pip install numpy
```

Prior to installing [geopandas via pip](https://geopandas.org/install.html#installing-with-pip) ``numpy`` must be installed, and 
a set of [wheels](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyproj) are required; shapely, fiona, pyproj, and rtree.  Use the 
command `pip install env\Scripts\{...}.whl` to install wheel files; the command assumes that the .whl files in question are hosted by env\Scripts\.

<br>

#### Requirements

In relation to requirements.txt

````markdown
    pip freeze -r docs/filter.txt > requirements.txt
````

The file [filter.txt](./docs/filter.txt) summarises the directly installed packages.  Hence, [filter.txt](./docs/filter.txt) is used 
to create a demarcated [requirements.txt](requirements.txt).  Note:

* scikit-learn is included for **releases** analysis purposes.  It is not used by `spots`, but it is used by `analysis.ipynb`, which 
is hosted by Google Colaboratory.  (Cf. `analysis.ipynb` and the `data.ipynb` file of this repository, then update these notes accordingly.)
* The above applies to `matplotlib` & `seaborn`
* `nodejs` cannot be included in `filter.txt`

<br>

#### Conventions

* pylint --generate-rcfile > .pylintrc


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

<br>
<br>

### Operating Systems Peculiarities

Beware of bash files created within a Windows environment.  The conversion

```bash
  dos2unix.exe *.sh
```

might be required.

