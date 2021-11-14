"""
s = (a+b+c)/2
A = Area
A = √s(s-a)(s-b)(s-c)
"""
import math
print("This program calculate the area of triangle.")
print("1.three side")
print("2.two sides and angle between them")

user_option = (input("Enter your options:"))

if user_option == '1':

    side1 = int(input("Enter first side: "))
    side2 = int(input("Enter second side: "))
    side3 = int(input("Enter third side: "))

    s = (side1+side2+side3)/2

    area = math.sqrt(s * (s-side1) * (s-side2) * (s-side3))


elif user_option == '2':
    side1 = int(input("Enter first side: "))
    side2 = int(input("Enter second side: "))
    angle = int(input("Enter angle: "))


    area = 0.5 * side1 * side2 * math.sin(math.radians(angle))



print("Area of Triangle is", area)