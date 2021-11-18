import re

nameage = """
Jakei is 22 and Theone is 23 
Cabriel is 44 and Joey 21
"""

names = re.findall(r'[A-Z][a-z]*', nameage)
ages = re.findall(r'\d{1,3}', nameage)

print("NamesAge :", nameage)
print("Find Name :", names)
print("Find Age :", ages)

print("Createe Dictionary")
dic = dict(zip(names,ages))
print("Dic :", dic)
