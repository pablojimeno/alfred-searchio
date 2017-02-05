#!/usr/bin/python
# encoding: utf-8
#
# Copyright (c) 2016 Dean Jackson <deanishe@deanishe.net>
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2016-03-13
#

"""Amazon variants."""

from __future__ import print_function, absolute_import

from collections import namedtuple
import json

from bs4 import BeautifulSoup as BS

from common import datapath, httpget, log, mkdata, mkvariant

url = 'https://www.wiktionary.org'
# path = datapath('Wiktionary.html')

SEARCH_URL = 'https://www.amazon.{tld}/gp/search?ie=UTF8&keywords={{query}}'
SUGGEST_URL = 'https://completion.amazon.{ctld}/search/complete?mkt={market}&method=completion&search-alias=aps&client=alfred-searchio&q={{query}}'

Store = namedtuple('Store', 'name lang country tld ctld market')
# Wiki = namedtuple('Wiki', 'id url lang name')


def stores():
    data = [
        {
          'name': u'United States',
          'lang': 'en',
          'country': 'us',
          'tld': 'com',
          'ctld': 'com',
          'market': 1
        },
        {
          'name': u'United Kingdom',
          'lang': 'en',
          'country': 'gb',
          'tld': 'co.uk',
          'ctld': 'co.uk',
          'market': 3
        },
        {
          'name': u'Canada',
          'lang': 'en',
          'country': 'ca',
          'tld': 'ca',
          'ctld': 'com',
          'market': 7
        },
        {
          'name': u'Deutschland',
          'lang': 'de',
          'country': 'de',
          'tld': 'de',
          'ctld': 'co.uk',
          'market': 4
        },
        {
          'name': u'France',
          'lang': 'fr',
          'country': 'fr',
          'tld': 'fr',
          'ctld': 'co.uk',
          'market': 5
        },
        {
          'name': u'España',
          'lang': 'es',
          'country': 'es',
          'tld': 'es',
          'ctld': 'co.uk',
          'market': 44551
        },
        {
          'name': u'Brasil',
          'lang': 'pt',
          'country': 'br',
          'tld': 'com.br',
          'ctld': 'com',
          'market': 526970
        }
    ]
    for d in data:
        # log('d=%r', d)
        s = mkvariant(d['country'],
                      d['name'],
                      u'Amazon {}'.format(d['name']),
                      SEARCH_URL.format(**d),
                      SUGGEST_URL.format(**d),
                      # icon='amazon.png',
                      # country=d['country'],
                      )
        yield s


def main():

    data = mkdata('Amazon', 'Online shopping')

    for s in stores():
        data['variants'].append(s)

    print(json.dumps(data, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
