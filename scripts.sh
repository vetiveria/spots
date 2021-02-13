#!/bin/bash

# A script file for Google Colaboratory


<<COMMENT
  Setting-up
COMMENT
# clean-up
rm -rf logs/ && rm -rf scripts/ && rm -rf src/

# prepare
mkdir logs



<<COMMENT
  Unload archives
  https://linux.die.net/man/1/wget
COMMENT
# scripts & src
wget -q https://github.com/vetiveria/spots/raw/develop/scripts.zip
wget -q https://github.com/vetiveria/spots/raw/develop/src.zip



<<COMMENT
  Dearchive
  https://linux.die.net/man/1/unzip

  In the case of a specific directory

    unzip -u -d -q directory src.zip

  wherein the options -u, -d, & -q denote update, specified directory, and quietly,
  respectively. Additionally, for archive content previewing purposes

    unzip -l src.zip
    unzip -v src.zip

COMMENT
# unzip scripts
unzip -u -q scripts.zip
rm -rf scripts.zip

# unzip src
unzip -u -q src.zip
rm -rf src.zip



<<COMMENT
  Install packages
COMMENT
# libspatialindex
chmod +x scripts/libspatialindex.sh
./scripts/libspatialindex.sh &> logs/libspatialindex.log

# rtree
chmod +x scripts/rtree.sh
./scripts/rtree.sh &> logs/rtree.log

# geopandas
pip install geopandas &> logs/geopandas.log

# dotmap
pip install dotmap &> logs/dotmap.log

# quantities
pip install quantities &> logs/quantities.log



<<COMMENT
  Later: TeX
COMMENT
# tex
# apt-get install texlive-latex-extra  &> logs/tex.log
# apt-get install ghostscript &>> logs/tex.log
# apt-get install dvipng &>> logs/tex.log