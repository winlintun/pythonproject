my_list = [4,10.5,'my_chat','my_chat']
print(my_list)
print(my_list[:2])

my_list[0] = 5
print(my_list)

print(my_list.index('my_chat'))#index number know
print(my_list.count('4'))#number_count


my_list.append('kyaw kyaw')#add
print(my_list)

my_list.pop()#remove (index number only)
print(my_list)

#my_list.pop(my_list.index(10.5))
#print(my_list)


#list(+)
my_list2 = [1,2,3]
print(my_list+my_list2)

 #sort
my_list2.sort()
print(my_list2)
#reverse
print(my_list2.reverse())
print(my_list2)

#list to str

list3 = ['my','name','is','mg chat.']
test = ''.join(list3)
print(type(test))
print(list3)

#loop
list = [[1,2],[3,4],[5,6]]
print(list[0])
print(list[-1][1])
list.append('abc')
print(list)
print(list[-1][2])

print()
print('Loop')
list4 = [[1,2],'abc']

for i in list4:
    print(i)