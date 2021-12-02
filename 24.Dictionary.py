#list []
#tuple ()
#dictionary {}

mg_chat = {'age': 21, 'gender': 'male','university':'MTU'}

print(mg_chat['age'])
print(mg_chat['gender'])
print("---------------------")
mg = {'mgmg':123}
i = 'mgmg'
j = 123
if i == mg[i]:
    print("hi")
    if j == mg[j]:
        print("done")
else:
    print("Faile")


print()
#add
mg_chat['native_town'] = 'magway'
print(mg_chat)

#remove
mg_chat.pop('age')
print(mg_chat)

#replace
mg_chat['age'] = '21' #add equal to replace he is overwrite

print(mg_chat.keys())
print('vluae', mg_chat.values())
print(mg_chat.items())

phone_price = {'iphone':{'12 min':'$699','12':'%799','12pro':'$999','12 pro max':'$1099'},
               'one plus':{'7':'700000','7 pro':'800000','8':'900000'}
               }

print(phone_price['iphone']['12 pro max'])
print(phone_price['one plus']['8'])

shop = {'laptop':['mac book','msi','acer','dell'],'printer':['canco','epson']   }

print(shop['laptop'])
print(shop['laptop'][0])

#for loop

for i in shop:
    print(i)#print(key)

print()
print()
for i in shop:
    print(shop[i])#value

print()
print()
for i in shop.values():
    print(i)#value

print()
print("---------------------")
for i,j in shop.items():
    print(i,end=':')
    print(j)
    #print key and value

print()
print()
for i in shop.items():
    print(i)
    # print key and value