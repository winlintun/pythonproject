
import csv
def menu():
    print("""
        Main Menu
    1. Create File
    2. Display The File
    3. Add New Items to the file
    4. Exit Program.""")

def createfile():
    filename = str(input("Enter File Name: "))
    file = open(filename, 'w')
    file.write("Name\t")
    file.write("Salar\t")

    file.close()

def displayfile():
    fielname = str(input("Enter File Name: "))
    file = open(fielname, 'r')
    print(file.read())

def addfile():
    filename = str(input("Enter File Name: "))
    file = open(filename, 'a')
    name = str(input("Enter Your Name: "))
    salary = str(input("Enter Your Salary: "))
    file.write("\n", name, "\t")
    file.write(salary, '\n')
    file.close()

try:
    a = int(input("Enter Number: "))
    if a == '1':
        createfile()
    elif a == '2':
        displayfile()
    elif a == '3':
        addfile()
    elif a == '4':
        print("Thank You!")
        exit()
    else:
        print("This number does not exit!")
        menu()
except ValueError:
    print("Enter Number Only!")
menu()
