import random
import time

smallest = 000
largest = 1000

random_number = random.randint(smallest, largest - 1)

#print(random_number)


#print()

def comb(L):

    for i in range(3):
        for j in range(3):
            for k in range(3):

                # check if the index are not
                # same
                if (i != j and j != k and i!= k):
                    print(L[i], L[j], L[k])

#user = list(input("enter 3 number: "))
#comb(user)

a = 0
b = 0
c = 0
for i in range(1, 2):
    smallest = 0
    largest = 10
    random_number = random.randint(smallest, largest - 1)
    a = random_number
    break

for j in range(1, 2):
    smallest = 0
    largest = 10
    random_number = random.randint(smallest, largest - 1)
    b = random_number
    break

for k in range(1, 2):
    smallest = 0
    largest = 10
    random_number = random.randint(smallest, largest - 1)
    c = random_number
    break

print(a,b,c)
comb([a, b, c])




