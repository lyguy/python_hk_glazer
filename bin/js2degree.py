#!/usr/bin/env python2

import argparse
import json_to_degree as js2deg

def main():
  """
  Command-line tool for json_to_degree
  """
  # Parse commandline options
  parser = argparse.ArgumentParser(description='Convert json formatted ' +
          'config files to valid input.dat config files ' +
          'for the Hock melt model.')

  parser.add_argument('input', type=str,
          help='json equivalent of input.dat')
  parser.add_argument('-o', '--output', type=str,
          help='output filename, if unspecified output is sent to stdout')

  parser.add_argument('-s', '--silent', action="store_true",
          default=False,
          help='silently overwrite <output>, if it exists')

  args = parser.parse_args()

  js2deg.json_to_dat(args.input, args.output, args.silent)

if __name__=="__main__":
  main()
