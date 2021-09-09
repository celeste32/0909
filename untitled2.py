# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 20:42:20 2021

@author: USER
"""
#威力彩  大樂透  38  49
import requests
from bs4 import BeautifulSoup
print("***威力彩***")
my_url = 'https://www.taiwanlottery.com.tw/index_new.aspx'
data = requests.get(my_url)
data.encoding = 'UTF-8'
data = data.text
Step0 = BeautifulSoup(data,'html.parser')
Step1 = Step0.find('div',class_='contents_box02')
Step2 = Step1.find_all('div',class_='ball_tx ball_green')
Step3 = Step1.find('div',class_='ball_red')
count=0
for i in Step2:
    count += 1
    if count > 6:
        print(i.text,end="")
print("特別號：",Step3.text)
print("*******"*7)
