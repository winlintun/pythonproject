import os
import platform

global lst
lst = ['Mg Mg', 'Hla Hla', 'Aye Aye', 'Kyaw Kyaw', "Mya Mya"]


bye = "\n Exiting Program! \n Thank You \n "


def schoomanagesystem():
    print("""
      ------------------------------------------------------
 |======================================================| 
 |======== Welcome To Student Management System	========|
 |======================================================|
  ------------------------------------------------------

Enter 1 : To Add Student,
Enter 2 : To View Student's List,
Enter 3 : To Search Student,
Enter 4 : To Remove Students
""")
    try:
        user = int(input("Please Select Option: "))

    except:
        print("Please enter between 1 or 4 numbers!")

    if user == 1:
        new = str(input("Enter Student Name: "))
        if new in lst:
            print("This {} student is Already in Database ".format(user))
        else:
            lst.append(new)
            print("Successful new add {} students".format(user))
            for i in lst:
                print("Updated Database ")
                print(i)
    elif user == 2:
        print("Students List\n")
        for i in lst:
            print(i)

    elif user == 3:
        search = str(input("Enter Student name to search: "))
        if search in lst:
            print("We Found at {} student.\n".format(search))
            for i in lst:
                print(i)
        else:
            print("Sorry! we can't found {} student in database!".format(search))
    elif user == 4:
        for i in lst:
            print(i)
        remove = str(input("Enter Student to remove: "))
        if remove in lst:
            lst.remove(remove)
            print('Successful to remove {} student.'.format(remove))
            for i in lst:
                print("Updated Database!\n")
                print(i)

        else:
            print("We can't found {} name in database!".format(remove))

schoomanagesystem()

def runagin():
    try:
        run = str(input("\nWant to run again: (y/n): "))

    except:
        print("Please yes or no!")

    if run == 'y' or run == 'Y':
        schoomanagesystem()
        runagin()
    elif run == 'n' or run == 'N':
        quit(bye)


runagin()