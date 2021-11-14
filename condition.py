firstnumber = input("Please first number : ")
secondnumber = input ("Please second number : ")

try :
    firstnumber = int(firstnumber)
    secondnumber = int(secondnumber)
    if secondnumber <= 0 :
        print ("Second number must be greater than 0")
    else:
        print (firstnumber, "divided by", secondnumber)
        print (firstnumber/secondnumber)
except ValueError:
    print ("Please enter number only")

#more condition
x = input("Enter First Number: ")
y = input("Enter Second Number: ")
try :
    x = int(x)
    y = int(y)
    if y <= 0 :
        print ("Second number must be greater tahn 0")
    elif y < 1 or y > 10 :
        print("Second number must be between 1-10")
    else:
        print(x, "divided by", y)
        print(x/y)
except ValueError:
    print("Please enter number only")
