

import pickle

one = ['I', 'am', 'one', 'here']
two = ['I', 'am', 'two', 'here', 'again']

with open ('data.dat', 'wb') as write:
    pickle.dump(one,write)
    pickle.dump(two,write)

with open('data.dat','rb') as read:
    read_one = pickle.load(read)
    read_two = pickle.load(read)

print("I am using cpickle \n", read_one, '\n', read_two)



with open('machine.data','w') as file:
    file.write('I am one here. \n')
    file.write('I am two here again.')

with open('machine.data', 'r') as file:
    for i in file.read():
        print(i, end='')
