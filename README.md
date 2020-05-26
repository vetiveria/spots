## Spots

Probable toxin release spots.

### Notes

These notes are updates continuously ...

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
    conda intall jupyterlab
    conda install nodejs
```

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


#### Standards

* pylint --generate-rcfile > .pylintrc


#### Misc

* https://jupyterlab.readthedocs.io/en/stable/index.html
* https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html

* https://docs.anaconda.com/anaconda/install/silent-mode/
* https://docs.anaconda.com/anaconda-adam/install/cloud/#installing-adam

* https://www.jetbrains.com/idea/download/other.html

* https://www.tecmint.com/18-tar-command-examples-in-linux/
