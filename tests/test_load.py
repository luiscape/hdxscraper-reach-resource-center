#!/usr/bin/python
# -*- coding: utf-8 -*-

# system
import os
import sys
dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(os.path.join(dir, 'scripts'))

# testing
import mock
import unittest
from mock import patch

# program
import collect.load as Load


class CheckLoadCountryList(unittest.TestCase):
  '''Unit tests for the loading of the country list.'''

  #
  # Check that load works.
  #
  def test_that_load_country_list_fails_gracefully(self):
    assert Load.LoadCountryList('xxx') == False
    assert Load.LoadCountryList() != False

  #
  # Testing object types.
  #
  def test_load_country_returns_array(self):
    d = Load.LoadCountryList()
    assert type(d) is list
