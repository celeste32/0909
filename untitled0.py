# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 19:39:44 2021

@author: USER
"""

import requests
from bs4 import BeautifulSoup

my_url = 'https://www.taiwanlottery.com.tw/index_new.aspx'
data = requests.get(my_url)
data.encoding = 'UTF-8'
data = data.text
Step0 = BeautifulSoup(data,'html.parser')
Step1 = Step0.find('div',class_='contents_box02')
Step2 = Step1.find_all('div',class_="ball_tx ball_yellow")
for i in Step2:
    print(i.text,end='')