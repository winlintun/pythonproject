print("****Welcome Beer House*******")


Age = int(input("What is your age: "))
Gender = input("Enter your Gendr (Male/Female): ")

if Age >= 18:
    if Gender == 'Male':
        print("You can buy Beer")
    elif Age >= 20:
        if Gender == 'Female':
            print("You can buy Beer")
    else:
        print("You can't buy Beer!")
else:
    print("Sorry! You can't buy Beer")