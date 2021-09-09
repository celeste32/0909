# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4  import BeautifulSoup

html_doc = """
<html><head><title>Hello World</title></head>
<body><h2>Test Header</h2>
<p>This is a test.</p>
<a id="it is ID link1" href="/my_link1">Link 1</a>
<a id="link2" href="/my_link2">Link 2</a>
<p>Hello, <b class="boldtext">Bold Text</b></p>
</body></html>
"""

soup = BeautifulSoup(html_doc,'html.parser')

h2 = soup.find('h2')
p = soup.find('p')
print(h2.text)
print(p.text)

h2_arr = soup.find_all('h2')
p_arr = soup.find_all('p')

print(h2_arr)
print(p_arr)

a = soup.find('a')

href1 = a.get('id')
print(href1)

alllink = soup.find_all('a')

for row in alllink:
    
    txt = row.text
    link = row.get('href')
    print(txt)
    print(link)
    print()
    
    









                      