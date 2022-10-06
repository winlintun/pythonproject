"""
# 4
reb = "Dany Boon"

def reverse(x):
    a = x.split(" ")
    print(a[1], a[0])

reverse(reb)

# 5
color_list = ["Red", "Green", "White", "Black"]
print(color_list[0], color_list[-1])


# 6
from datetime import datetime
exam_date = datetime(2014,12,11)
print(exam_date.strftime("%d/%m/%Y"))




# 8
num = int(input("Enter number: "))

if num % 2 == 0:
    print("even number.")
else:
    print("Odd number.")


# 9
height = int(input("Enter height: "))
base = int(input("Enter base: "))

area = (base * height) * 0.5
print("Area: ", area)

# 10
x = 10
y = 6

def add(x, y):
    total = x + y
    if total <= 20:
        return 20
    else:
        return total

print(add(x, y))

# 11

first = int(input("Enter first value: "))
op = input("Enter operator(+,-): ")
second = int(input("Enter second value: "))

if op == "+":
    result = first + second
else:
    result = first - second

if result == 5:
    print(True)
else:
    print(False)

# 12
name = input("Enter your name: ")
age = int(input("Enter your age: "))
address = input("Enter your address")

print(f"""
name: {name}
age: {age}
address: {address}
""")

# Loop
# 1
while True:
    print(10)


# 2 -> 2
n = int(input("Enter n: "))
result = 0

for i in range(n+1):
    result += i

print(result)


# 3
n = int(input("Enter number: "))

for i in range(n):
    print(i, end='\t')


# 4
list1 = [12, 15, 32, 42, 55, 75, 122,]

temp= 0

for i in list1:
    if i % 5 == 0:
        temp = i + i
        if temp > 150:
            break
        print(i)

print(temp)


# 5
for i in range(10):
    a = -10
    a += i
    print(a)

# 7
#n = int(input("Enter number"))
n = 5

n1 = int(("%s" % n))
n2 = int(("%s%s" % (n, n)))
n3 = int(("%s%s%s" % (n,n,n)))

print(n1+n2+n3)

"""



