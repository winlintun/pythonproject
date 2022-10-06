import random
from datetime import datetime
import os



def most_frequent(list_data):
    return max(set(list_data), key = list_data.count)

def start_now():
    start = datetime.now()

    data1 = []

    small = 000
    large = 999

    while large > small:
        #for i in range(000, 1000):
        a = random.randint(000, 999)
        data1.append(a)
        large -= 1
    #print(data1)
    data1 = most_frequent(data1)
    #data = [data1, data2, data3]

    #print()
    #print('most frequence\n')
    end = datetime.now()

    second = (end - start) / 1000

    print("Time: ", second, 'second')
    print()

    data1 = str(data1)
    return data1

if os.name == 'nt':
    os.system('cls')

#if datetime.now().strftime('%M') != '30':
for i in range(3):
    print(start_now())


input("Press Any Key")
