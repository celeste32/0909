# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 21:28:36 2021

@author: USER
"""

import requests
from bs4 import BeautifulSoup
url = 'https://www.esunbank.com.tw/bank/personal/deposit/rate/forex/foreign-exchange-rates'
data = requests.get(url)
data.encoding = "UTF-8"
data = data.text
rates = BeautifulSoup(data,'html.parser')
allCoins = rates.find(id='inteTabel1')
CountryRate = rates.find_all('tr',class_='tableContent-light')
for i in CountryRate:
    tds = i.find_all('td')
    for r in tds:
        print(r.text)