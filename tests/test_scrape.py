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
import collect.scrape as Scrape

class TestScraper(unittest.TestCase):
  '''Unit tests that the scraper is collecting data.'''

  #
  # Check that load works.
  #
  def test_scraper_doesnt_fail(self):
    assert Scrape.ScrapeReachCountryList('AF') == False
    assert Scrape.ScrapeReachCountryList('SY') != False

  #
  # Testing object types.
  #
  def tets_scraped_data_contains_the_right_schema(self):
    d = Scrape.ScrapeReachCountryList('AF')
    assert d[0].get('Date', None) != None
    assert d[0].get('URL', None) != None
    assert d[0].get('Title', None) != None
