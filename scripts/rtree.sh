#!/bin/bash

# Package parameter
package=Rtree-0.9.4

# Unpack
curl -L https://files.pythonhosted.org/packages/56/6f/f1e91001d5ad9fa9bed65875152f5a1c7955c5763168cae309546e6e9fda/${package}.tar.gz | tar xz

# Set-up
cd ${package} && /usr/local/bin/python setup.py install
