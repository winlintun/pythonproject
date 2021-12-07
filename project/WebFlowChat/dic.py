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

print()


prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
def compute_bill(food):
    total = 0
    for item in food:
        total += prices[item]
    print(total)
    return total


shopping_list = ["banana", "orange", "apple"]

compute_bill(shopping_list)