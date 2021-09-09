# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 20:05:32 2021

@author: USER
"""

import requests
from bs4 import BeautifulSoup
url = 'https://www.setn.com/ViewAll.aspx?PageGroupID=0'
data = requests.get(url)
data.encoding = "UTF-8"
data = data.text
results = BeautifulSoup(data,'html.parser')
allNews = results.find_all('div',class_="col-sm-12 newsItems")
for i in allNews:
    time = i.find('time').text
    h3 = i.find('h3')
    title = h3.find('a').text
    link = h3.find('a').get('href')
    print(time,title,link,end="\n")