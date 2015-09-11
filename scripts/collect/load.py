#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv

def LoadCountryList(path='data/countries.csv'):
  '''Load the country list from the local data folder.'''

  #
  # Creating an array of objects.
  #
  out = []
  try:
    with open(path, 'rb') as f:
      data = csv.DictReader(f)
      for row in data:
        out.append(row)

  except Exception as e:
    print e
    return False

  #
  # Returning the array of
  # objects.
  #
  return out
