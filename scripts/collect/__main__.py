#!/usr/bin/python
# -*- coding: utf-8 -*-

import load
import store
import scrape

def Main():
  '''Wrapper.'''

  country_list = load.LoadCountryList()

  data = []
  for country in country_list:
    country_data = scrape.ScrapeReachCountryList(country['iso'])

    #
    # Adds country code
    # and country name.
    #
    if country_data != False:
      for record in country_data:
        record.update(iso=country['iso'], name=country['name'])

      data += country_data

  store.StoreRecords(data)


if __name__ == '__main__':
  Main()
