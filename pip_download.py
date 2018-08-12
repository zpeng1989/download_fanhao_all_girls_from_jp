# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 08:30:47 2018

@author: zpeng
"""

import sys
import time
import urllib
import urllib.request
import requests
import numpy as np
from bs4 import BeautifulSoup
import doenload_mid

#Some User Agents
hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]

url='http://nanrenvip.org/find.html'

req = urllib.request.Request(url)
source_code = urllib.request.urlopen(req).read()
plain_text=str(source_code)

soup = BeautifulSoup(plain_text)

list_soup = soup.find('div', {'class': 'inner'})

for book_info in list_soup.findAll('li'):
    book_url = book_info.find('a').get('href')
    #baseurl = r'http://nanrenvip.org/baishimolinai'
    book_url = book_url.strip().strip('html')
    print(book_url)
    if(len(book_url)>5):
        baseurl = r'http://nanrenvip.org/%s'%book_url
        print(baseurl)
        newurl = "http://nanrenvip.org"
        try:
            S = AVNY(baseurl,newurl)
            S.strat()
        except:
            print('error')
        #print(book_url)

#print(list_soup)
