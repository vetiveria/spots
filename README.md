## Spots

Probable toxin release spots.

<br>
<br>

### Notes

These notes are updates continuously ...

<br>
<br>

#### A different approach

Environments
* https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

Ensure that pip's version is ≥ 20.0.2.  Also required: [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

```bash
python -m venv env
env\Scripts\activate.bat
python -m pip install --upgrade pip==20.1.1
pip install numpy
```

<br>

Installing `geopandas` via pip
* https://geopandas.org/install.html#installing-with-pip

<br>

Wheels
* https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyproj

Use the command `pip install env\Scripts\{...}.whl` to install wheel files; the command assumes that the .whl files in question are hosted by env\Scripts\

<br>

**Before installing** the wheels of shapely, fiona, pyproj, and rtree, install

* numpy

<br>
<br>

#### Installing Packages

Ideas, courtesy of geopandas, as https://geopandas.org/install.html

```markdown
    conda create --prefix ...environment
    conda activate environment

    conda config --env --add channels conda-forge
    conda config --env --set channel_priority strict
    conda install python=3.7 geopandas
```
and then

```markdown
    conda install geopy
    conda install pywin32
    conda install pytest
    conda install coverage
    conda install pytest-cov
    conda install pylint
    conda install pyyaml
    conda install requests
    conda install jupyterlab
    conda install nodejs
```

<br>
<br>

#### The Requirements

````markdown
    pip freeze -r docs/filter.txt > requirements.txt
````

The file [filter.txt](./docs/filter.txt) summarises the directly installed packages, e.g.,

* pip
* geopandas
* pytest
* coverage
* pytest-cov
* pylint
* PyYaml

Hence, [filter.txt](./docs/filter.txt) is used to create a demarcated [requirements.txt](requirements.txt)

<br>
<br>

#### Standards

* pylint --generate-rcfile > .pylintrc

<br>
<br>

#### Misc

* https://jupyterlab.readthedocs.io/en/stable/index.html
* https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html

* https://docs.anaconda.com/anaconda/install/silent-mode/
* https://docs.anaconda.com/anaconda-adam/install/cloud/#installing-adam

* https://www.jetbrains.com/idea/download/other.html

* https://www.tecmint.com/18-tar-command-examples-in-linux/
