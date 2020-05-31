#!/bin/bash

apt-get install -qq curl g++ make

# Parameters
version=1.9.2
package=spatialindex-src-$version
directory="/usr/local/"

# Download & unpack tar
curl -L https://github.com/libspatialindex/libspatialindex/releases/download/$version/$package.tar.gz | tar xz

# Switch directory
cd $package

# make
cmake -DCMAKE_INSTALL_PREFIX=$directory .
make
make install

cp ${directory}lib/libspatialindex* /lib/