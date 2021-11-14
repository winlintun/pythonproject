import fileinput


def menu():
    print("""
        Main Menu
    1. Create File
    2. Display File
    3. Add new items to the file
    4. Exiting Program!
    
    """)
menu()

def creatfile():
    aa = input("Enter File Name: ")
    file = open(aa.txt,'w')
    file.write("Name\t")
    file.write("Salary\t")
    file.close()

def displayfile():
    print("Dispaly File:",creatfile())
    file = open(creatfile(),'r')
    print(file.read(creatfile()))
    file.close()

def addfile():
    file = open(creatfile(),'a')
    name = input("Enter Your Name: ")
    salary = input("Enter Your Salary: ")
    file.write('\n',name,'\t')
    file.write(salary,'\n')
    file.close()



try:
    user_input = str(input("Choose Options: "))
    if user_input == '1':
        creatfile()
    elif user_input == '2':
        pass
    elif user_input == '3':
        pass
    elif user_input == '4':
        print("Thank You!")
        exit()
    else:
        print("Wrong Number!")
        print("Try Again!")
except ValueError:
    print("Please Enter Number Only!")
menu()