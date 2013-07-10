**hk_glazer** [![Build Status](https://travis-ci.org/fmuzf/meltmod_jsontodegree.png?branch=master)](https://travis-ci.org/fmuzf/python_hk_glazer)
====================

This is a part of the Hock Melt Model: a tool to convert between json config
files and valid input.dat


## Installation

1. Download:

        $ git clone https://github.com/fmuzf/python_hk_glazer.git

2. Install:

        $ python setup.py install

3. Done.

# Command-Line Usage:

      $ hk_glazer <js2degree/degree2js> [-h] [-o OUPUT] [-s] entry

Convert json formatted config files to valid input.dat config files for the
Hock melt model.

positional arguments:

  entry:                configuration be it json or txt

optional arguments:

  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT output filename, if unspecified output is sent to stdout
  -s, --silent          silently overwrite OUTPUT, if it exists
