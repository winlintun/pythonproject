import re

txt = "The rain in Spain"

x = re.findall("Portugal", txt)
print(x)


s = re.search("\s", txt)
print("The first white-space char is located in position: ", s.start())


se = re.search("Portugal", txt)
print(se)


sp = re.split("\s", txt)
print(sp)


su = re.sub("\s", "9", txt)
print(su)


see = re.search(r"\bS\w+", txt)
print(see.group())
