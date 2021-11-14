user_num=int(input("Enter your number: "))
my_num=int(100)


if user_num>my_num:
    print("Your nubmer is greater than my number!")
elif user_num<my_num:
    print("Your number is less than my number!")

else:
    print("you number is the same as my number!")

print()
print()
mark=int(input("Enter you mark: "))

if mark>90:
    grade='A'
elif mark>=80:
    grade='B'
elif mark>70:
    grade='C'
else:
    grade='D'
print('Your grade is ',grade)