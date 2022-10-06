# startDay = int(input("Enter the start day of month (1-7): "))
# num_of_days = int(input("Enter number of days: "))

# print("Sun Mon Tues Wed Thurs Fir Sat")
# print("------------------------------")
# i = startDay-1 # 2-1 = 1

# for j in range(1, num_of_days+1):
# 	if i>6:
# 		print()
# 		i = 1
# 	else:
# 		i += 1
# 	print(str(j) +"		", end='	')


# 1. Determine wether a person is eligible to vote
# Program >

# age = int(input("Enter the age: "))
# if (age>= 18):
#     print("You are eligible to vote")

# 2. Write a program to determine the character entered by the user
# Program >

# char = input('Press any Key: ')
# if (char.isalpha()):
#     print("Ther user has entered a character")
# if (char.isdigit()):
#     print("The user has entered a digit")
# if (char.isspace()):
#     print("Ther user entered a while space character")

# 3. Write a Program to determine whether a person is eligible to vote or note. if he is not
# eligible, display how many year are left to be eligible.
# Program >

# age = int(input("Enter the age: "))
# if (age>=18):
#     print('You are eligible to vote')
# else:
#     yrs = 18 - age
#     print("Your have to wait for another "+ str(yrs)+ " years to cast your vote")
    
# 4. Write a program to find larger of two number
# program> 

# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))

# if (a>b):
#     large = a
# else:
#     large = b
# print("Large = ", large)

# 5. Write a program to find whether the given number is even or odd.
# program >

# num = int(input("Enter any number: "))

# if (num % 2 == 0):
#     print(num, 'is even')
# else:
#     print(num, 'is odd')

# 6. Write a program to enter any character. If the entered character is in lowercase then
# convert it into uppercase and if it an uppercase characeter, the converted it into lower case
# program >

# ch = input('Enter any character: ')

# if (ch >= 'A' and ch <= 'Z'):
#     ch = ch.lower()
#     print('The enter character was in uppercase. In lowercase it is : ' + ch)
# else:
#     ch = ch.upper()
#     print('The enter character was in lowercase. In upptercase it is : ' + ch)

# 7. A company decides to give bonus to all its employees on Diwali. A 5% bonus on salary is given
# to the male workers and 10% bonus on salary ot the female workers.
# Write a program to enter the salary of the employee and sex of the employee. If the salary
# of the employee is less than $ 10000 then the employee gets an extra 2% bonus on salary. 
# Calcuate the bonus than has to be given to the employee and display the salary theat the 
# employee will get.
# program start >

# ch = input('Enter the sex of the employee (m or f) : ')
# sal = int(input("Enter the salary of the employee : "))

# if (ch == 'm'):
#     bonus = 0.05 * sal 
# else:
#     bonus = 0.10 * sal 

# amt_to_be_paid = sal + bonus
# print("Salary = ", sal)
# print("Bonus = ", bonus)
# print("************************")
# print("Amount ot paid : ", amt_to_be_paid)

# 8. Write a program to find whether a give year is a leap year or not.
# program start >

# year = int(input("Enter any year: "))

# if ((year % 4 == 0 and year % 100 != 0) or (year % 4 == 0)):
#     print(year, " is Leap year")
# else:
#     print(year, 'is not leap year')

# 9. Program that prompts the user to enter a number and then print its interval
# program start >

# num = int(input("Enter any number fromn 0-30: "))

# if (num>=0 and num<10):
#     print("It is in the range 0-10")
# if (num>=10 and num<20):
#     print("It is in the range 10-20")
# if (num>=20 and num<30):
#     print("It is in the range 20-30")
    
# 10. Program to test whether a number entered by the user is negative, positive, or equal to zero
# program start >

# num = int(input("Enter any number: "))

# if (num == 0):
#     print("The value is equal to zero")
# elif (num>0):
#     print("The number is posistive")
# else:
#     print("The number is negative")

# 11. Write a program to determine whether the character entered is a vowel or not
# program start >

# ch = input("Enter any character: ")

# if (ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
#     print(ch, 'is a vowel')
# elif (ch == 'a' or ch == 'e' or ch =='i' or ch == 'o' or ch == 'u'):
#     print(ch, 'is a vowel')
# else:
#     print(ch, 'is not a vowel')

# 12. Write a program to find the greatest number from three numbers.
# program start >

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))

# if (num1>num2):
#     if(num1>num3):
#         print(num1, 'is greater than', num2,'and', num3)
#     else:
#         print(num3, 'is greater than', num1, 'and', num2)
# elif (num2>num3):
#     print(num2, 'is greate than', num1, 'and', num3)
# else:
#     print("Three number are equal")

# 13. Write a program that prompts the user to enter a number between 1-7 and then display
# the corresponding day to the week.
# program start >

# num = int(input("Enter any number between 1 to 7: "))

# if (num==1): print('Sunday')
# elif (num==2): print('Monday')
# elif (num==3): print('Tuesday')
# elif (num==4): print('Wednesday')
# elif (num==5): print('Thursday')
# elif (num==6): print('Friday')
# elif (num==7): print('Saturday')
# else:
#     print('Wrong input')

# 14. Write a program to take input from the user and then check whether it is a number or
# a character. If it is a character, determine whether it is in uppercase or lowercase.
# program start >

# ch = input("Enter the character: ")

# if ch>= 'A' and ch <= 'Z':
#     print('Uppercase character was entered')
# elif ch >= 'a' and ch <= 'z':
#     print("Lowercase character was entered")
# elif ch >= '0' and ch <= '9':
#     print('A number was entered')

# 15. Write a program to calculate roots of a quadratic equation
# program start >

# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))
# c = int(input("Enter the value of c: "))

# D = (b*b) - (4*a*c)

# if D > 0:
#     print("Real Roots")
#     root1 = (-b + D**0.5) / deno
#     root2 = (-b - D**0.5) / deno
#     print("Root1 = ",root1, '\tRoot2 = ', root2)
# elif D == 0:
#     print("EQUAL ROOTS")
#     root1 = -b / deno
#     print('Root1 and Root2 = ', root1)
# else:
#     print("IMAGINARY ROOTS")

# White Loop
# 1. Program to print first 10 numbers using a while loop
# program start >

# i = 0 
# while (i<=10):
#     print(i, end=' ')
#     i += 1

# 2. Program to sparate two value printed on the same line using a tab 
# program start >

# i = 0
# while i <= 10:
#     print(i, end='\t')
#     i += 1

# 3. Write a program to calculate the sum and average of first 10 numbers.
# program start >

# i = 0
# s = 0
# while i <= 10:
#     s = s + i
#     i += 1
# avg = float(s)/10
# print("The sum of first 10 number is : ",s)
# print('The average of first 10 number is: ', avg)

# 4. Write a program to print 20 horizontal astersks (*).
# program start >

# i = 1
# while i <= 20:
#     print("*", end='')
#     i += 1

# 5. Write a program to calcuate the sum of numbers from m to n
# program start >

# m = int(input("Enter the value of m: "))
# n = int(input("Enter the value of n: "))
# s = 0

# while m <= n:
#     s += m
#     m = m + 1
# print("Sum = ", s)

# 6. Write a program to enter a decimal number. Calculate and display the binary
# equivalent of this number
# program start >

# decimal_num = int(input("Enter the decimal number: "))
# binary_num = 0
# i = 0
# while decimal_num != 0:
#     remainder = decimal_num % 2
#     binary_num = binary_num + remainder*(10**i)
#     decimal_num /= 2
#     i = i + 1
# print('The binary equivalent =', binary_num)

# 7. Write a program to read a character until a * is encountered. Also count the number of 
# uppercase, lowercase, and numbers entered by the users.
# program start >

# ch = str(input("Enter any character: "))
# num_count = 0 
# up_count = 0
# lowe_count = 0

# if ch >= '0' and ch <= '9':
#     num_count += 1
# elif ch >= 'a' and ch <= 'z':
#     lowe_count += 1
# elif ch >= 'A' and ch <= 'Z':
#     up_count += 1
# while ch != '*':
#     ch = input("Enter any character: ")
#     if ch >= '0' and ch <= '9':
#         num_count += 1
#     elif ch >= 'a' and ch <= 'z':
#         lowe_count += 1
#     elif ch >= 'A' and ch <= 'Z':
#         up_count += 1
# print("Number of lowercase characters are: ", lowe_count)
# print('Number of uppercase characters are: ', up_count)
# print('Number of numerial are: ', num_count)

# 8. Write a program to enter a number and then calculate the sum of its digits.

# sum_of_digit = 0
# num = int(input("Enter the number: "))
# while num != 0:
#     temp = num % 10
#     sum_of_digit += temp
#     num = num / 10
# print('The sum of digit is :',sum_of_digit)

# For Loop
# 1. Program to print first n number using the range() in a for loop.
# program start >

# for i in range(1, 5):
#     print(i, end=' ')

# for i in range(1, 10, 2):
#     print(i, end=' ')
# 2. Write a program to print the following pattern.
# ****************
# ****************
# ****************
# ****************
# ****************
# program start >

# for i in range(5):
#     print()
#     for j in range(5):
#         print('*', end='')

# 3. Write a program to print the following pattern.
# *
# **
# ***
# ****
# *****
# program start >

# for i in range(1, 6):
#     print()
#     for j in range(i):
#         print('*', end='')

# 4. Write a program to print the following pattern
# 1
# 1   2
# 1   2   3
# 1   2   3   4
# 1   2   3   4   5
# program start >
# for i in range(1, 6):
#     print()
#     for j in range(1, i+1):
#         print(j, end='  ')

# 5. Write a program to print the following pattern.
# 1
# 22
# 333
# 4444
# 55555
# program start >

# for i in range(1, 6):
#     print()
#     for j in range(1, i+1):
#         print(i, end='')

# 6. Write a program to print the following pattern
# 0
# 12
# 345
# 6789
# program start >

# count = 0
# for i in range(1, 5):
#     print()
#     for j in range(1, i+1):
#         print(count, end='')
#         count = count + 1

# 7. Write a program to print the following pattern.
#                 1
#             12
#         123
#     1234
# 12345
# program start >

# N = 5
# for i in range(1, N+1):
#     for k in range(N, i, -1):
#         print(' ', end=' ')
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print()

# 8. Write a program to print the following pattern.
#                 1
#             1   2   1
#         1   2   3   2   1
#     1   2   3   4   3   2   1
# 1   2   3   4   5   4   2   2   1
# program start >
N = 5
for i in range(1, N+1):
    for k in range(N, i, -1):
        print(" ", end=' ')
    for j in range(1, i+1):
        print(j, end=' ')
    for l in range(1-1, 0, -1):
        print(l, end=' ')
    print()