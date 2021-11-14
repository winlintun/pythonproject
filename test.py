
"""
import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.mydarksitecollection.online/")
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text

import requests
from bs4 import BeautifulSoup

# http://www.gad.gov.mm/en/content/data?destination=content/data
page = requests.get('https://oxylabs.io/blog/python-web-scraping')
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find('href')

print(table)

#print(soup.find('table'))
#print(soup)

"""

import requests
from bs4 import BeautifulSoup
#import re


url = 'https://channelmyanmar.org/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

links = soup.select('table tbody tr td.titleColumn a')
first = links[:10]
for i in first:
    print(i.text)


"""
1>git config --global user.name 'iceface'
2>git config user.email 'www.iceface@gmail.com'
3>git config user.name # check username
4> git config user.email # check email
create  repo
5>git init 
exist projectfile using git
6>git init
show modif
7>git status
remove modif
8>git rm --cache (filename)
#git add many file and many folder
9>git add .

"""