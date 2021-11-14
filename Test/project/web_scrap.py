
"""

import requests
from bs4 import BeautifulSoup
import re

result = requests.get('https://osp.wunzinn.com/book_by_series/V0Yzc2txSWVuTWpFUmxCMExtcjhZQT09')

content = result.content

soup = BeautifulSoup(content, features='lxml')

sample = soup.select('#rso > div:nth-child(1) > div > div > div > div > div > div.yuRUbf > a > h3')

a = soup.find_all("a")

#print(soup.prettify())


#print(a)
b = []
for i in a:
    b = soup.find_all('href')
    b.append(i)
   # print(list(b))

"""
import requests
from bs4 import BeautifulSoup

# python3 -m pip install requests
# python3 -m pip install beautifulsoup4
URL = "https://osp.wunzinn.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

result = soup.find_all('a')


for i in result:
    print(i.get('href'))