# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 21:26:36 2021

@author: USER
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.esunbank.com.tw/bank/personal/deposit/rate/forex/foreign-exchange-rates'

data = requests.get(url)

data.encoding = 'UTF-8'

data = data.text

sp = BeautifulSoup(data,'html.parser')

rate = sp.find(id='inteTable1')

countryR = rate.find_all('tr',class_='tableContent-light')
for row in countryR:
    tds = row.find_all('td')
    
    print(tds[0].text)