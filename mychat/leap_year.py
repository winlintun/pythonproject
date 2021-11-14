print("This program determines whether leap years or not!")

year = int(input("Enter year: "))

if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("This year is leap year")
        else:
            print("This year is not leap year")
    else:
        print("This year is a leap year!")


else:
    print("This year is not leap year")