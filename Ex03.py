# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 20:04:41 2021

@author: USER
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.setn.com/ViewAll.aspx?PageGroupID=0'

data = requests.get(url)

data.encoding = 'UTF-8'

data = data.text

sp = BeautifulSoup(data,'html.parser')

allNews = sp.find_all('div',class_='col-sm-12 newsItems')

for row in allNews:
    t = row.find('time').text
    
    h3 = row.find('h3')    
    title = h3.find('a').text
    link = h3.find('a').get('href')
    
    
    print(title)
    print(link)
    print(t)