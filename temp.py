# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup

html_doc = '''
<html><head><title>Hello World</title></head>
<body><h2>Test Header</h2>
<p>This is a test.</p>
<a id="link1" href="/my_link1">Link 1</a>
<a id="link2" href="/my_link2">Link 2</a>
<p>Hello, <b class="boldtext">Bold Text</b></p>
</body></html>
'''
soup = BeautifulSoup(html_doc,'html.parser') #parser 解析、解譯
H = soup.find('h2')
P = soup.find('p')
print(H.text)
print(P.text)
H_arr = soup.find_all('h2')
P_arr = soup.find_all('p')
print(H_arr)
print(P_arr)

print("*"*30)

a = soup.find('a')
a_text = a.text
href1 = a.get('href')
print(a_text)
print(href1)

print("*"*30)

all_link = soup.find_all('a')
for i in all_link:
    txt = i.text
    link = i.get('href')
    print(txt)
    print(link)

print("*"*30)


    