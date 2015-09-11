#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def ScrapeReachCountryList(country_code, filter_data=True, verbose=True):
  '''Scrapes REACH's webiste and assembles a list of dataset per country.'''

  print "Scraping the REACH website: %s." % country_code

  #
  # Assemble URL.
  #
  f = '&field_document_type_tid[]=6'
  u = 'http://www.reachresourcecentre.info/advanced-search?name_list[]=%s' % country_code
  if filter_data:
    u += f

  try:

    #
    # Download data from Motivate's website.
    #
    r = requests.get(u)

    #
    # Find data with BeautifulSoup.
    #
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.findAll("tbody")

    keys = ['Title', 'Date', 'URL']
    out = []
    i = 0
    for row in table[0].findAll('tr'):

      col = [ d.text for d in row.findAll('td') ]

      #
      # Finds href.
      #
      l = row.findAll('td')[0].findAll('a', href=True)[0]['href']

      col.append(l)

      out.append(dict(zip(keys, col)))


      i += 1

    return out


  except Exception as e:
    print "Failed to scrape data from REACH website"
    print e
    return False

