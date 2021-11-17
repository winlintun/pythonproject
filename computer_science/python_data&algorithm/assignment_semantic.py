str1 = 'Hello'
str2 = str1
print("Immutable")
a = 10
b = a

a += 1
print("B ", b)
print("A ", a)

print("Mutable")
lst = [100, 200]

lst_two = lst # reference
lst.append(300)
lst_two.append(400)

print("Lst ", lst, 'Id ', id(lst))
print("lst_two ", lst_two, 'Id ', id(lst_two))

print()

lst_two = [400, 500] # create object
lst_two.append(600)
print("Lst ", lst, 'Id ', id(lst))
print("lst_two ", lst_two, 'Id ', id(lst_two))
