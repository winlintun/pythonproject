import requests
import re
#https://buildmedia.readthedocs.org/media/pdf/python-textbok/1.0/python-textbok.pdf
url = input("Enter url: ")
 
page = requests.get(url)

a = '.pdf'
find = re.findall('\.pdf', page)

print(find)

# with open("ubuntu.iso", 'wb') as f:
#     f.write(page.content)