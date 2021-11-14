import random

my_num = random.randrange(51)
chance = 5
print("You chance is = ", chance)
print("My number between 1 to 50")
your_num = int(input("Enter number : "))

while your_num != my_num and chance > 1:

    if your_num > my_num:
        print("Your number is greater than my number")

    elif your_num < my_num:
        print("Your Number is less than my number")

    else:
        print("Sorry! Wrong Answer")
    print()

    chance = chance - 1
    print("You chance is = ", chance, 'chances')
    your_num = int(input("enter number: "))

if your_num == my_num:
    print("Coagulation! You got it.")
else:
    print("My number is = ", my_num)
    print("Please Try Again!")
