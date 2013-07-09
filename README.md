**jsontodegree** [![Build Status](https://travis-ci.org/fmuzf/meltmod_jsontodegree.png?branch=master)](https://travis-ci.org/fmuzf/meltmod_jsontodegree)
====================

This is a part of the Hock Melt Model: a tool to convert json config files to valid input.dat


## Installation

1. Download:

        git clone https://github.com/fmuzf/meltmod_jsontodegree.git

2. Install:

        $ python setup.py install

3. Done.

# Usage:

    json_to_degree.py [-h] [-o OUTPUT] [-s] input

Convert json formatted config files to valid input.dat config files for the
Hock melt model.

positional arguments:
  input:                json equivalent of input.dat

optional arguments:

  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT output filename, if unspecified output is sent to stdout
  -s, --silent          silently overwrite OUTPUT, if it exists
