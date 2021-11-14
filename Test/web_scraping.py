"""
from bs4 import BeautifulSoup
import requests

url = 'https://www.tohg-mm.xyz/'

# Getting the webpage, creating a Response object.
response = requests.get(url)

# Extracting the source code of the page.
data = response.text

# Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
soup = BeautifulSoup(data, 'lxml')

# Extracting all the <a> tags into a list.
tags = soup.find_all('a')

# Extracting URLs from the attribute href in the <a> tags.
#for tag in tags:
 #   print(tag.get('href'))

print(data)

"""

import requests
from bs4 import BeautifulSoup
import re

result = requests.get('https://www.tohg-mm.xyz/')

content = result.content

soup = BeautifulSoup(content, features='lxml')

sample = soup.select('#rso > div:nth-child(1) > div > div > div.yuRUbf > a > h3')

a = soup.find_all("a")

#print(soup.prettify())


#print(a)

for i in a:
    print(i)