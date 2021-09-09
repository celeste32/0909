# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 19:39:07 2021

@author: USER
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.taiwanlottery.com.tw/index_new.aspx'

data = requests.get(url)

data.encoding = 'UTF-8'

data = data.text

sp = BeautifulSoup(data,'html.parser')

ball = sp.find('div',class_='ball_box01')

numbers = ball.find_all('div',class_='ball_tx ball_yellow')

for row in numbers:
    print(row.text,end=',')
print()    
print('-'*40)

allitem = sp.find_all('div',class_='contents_box02')

count = 0
for row in allitem:
    if count % 2 == 0:
        greens = row.find_all('div',class_='ball_tx ball_green')
        red = row.find('div',class_='ball_red')
        for num in greens:
            print(num.text,end=',')
        print(red.text)    
        print()    
        
    
    count+=1
    
    






