dic = {}
u = 'mgmg'
p = 123

dic[u] = p
print("Adding ", dic)

print('key :', dic.keys())
print('value: ', dic.values())
print()
if u in dic:
    print('done')
    if p in dic.values():
        print('done')

else:
    print('faile')
