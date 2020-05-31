## Spots

Probable toxin release spots.

<br>
<br>

### Notes

These notes are updates continuously ...

<br>
<br>

#### Bash

Beware of bash files created within a Windows environment.  The conversion

```bash
  dos2unix.exe *.sh
```

might be required.

<br>
<br>

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

  conda install -c anaconda python=3.7.7 geopandas geopy nodejs jupyterlab pywin32 pytest coverage pytest-cov pylint pyyaml    
```

Next time set-up

```bash
  conda config --env --add channels anaconda
  conda config --env --set channel_priority strict
```

<br>
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
<br>



#### The Requirements

````markdown
    pip freeze -r docs/filter.txt > requirements.txt
````

The file [filter.txt](./docs/filter.txt) summarises the directly installed packages.  Hence, [filter.txt](./docs/filter.txt) is used to create a demarcated [requirements.txt](requirements.txt)

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
