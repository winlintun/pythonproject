"""

class Login:
    user_database = {}

    def Sing_In(self):
        try:
            username = str(input("Enter your name: "))
            password = int(input("Enter your password: "))

            Login.user_database[username] = password

            if username in Login.user_database:
                print("Successful\n")
                print(Login.user_database)

            else:
                print("Your account is exist!")
                print("Try Again")
        except ValueError:
            print("Wrong Input Error!")

    def Sing_Up(self):
        username = str(input("Enter your name: "))
        password = int(input("Enter your password: "))

        if username in Login.user_database:
            print("Successful!\n")

        elif username not in Login.user_database:
            print('Not Found {} user '.format(username))

    print(user_database)

class User (Login):
    def __init__(self):
        print("Welcome User Login")
        choose = int(input("(Singin = 1 / Singup = 2): "))
        if choose == 1:
           User.Sing_Up()
        elif choose == 2:
            User.Sing_Up()


user = Login()
user.Sing_Up()
user.Sing_In()

"""


class User:
    global user_database

    user_database = {} # empty dictionary

    def __init__(self):
        print("Welcome")

    def user_register(self):
        print("Register Page ")
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username not in user_database:
            user_database[username] = password
            print("Create account is successful")
            print(f">>>Your account<<<\n username:{username}\n password:{password}\n")
            print("------------------------------------------------")
        elif username in user_database:
            print("Your {} account is exist!".format(username))
            print("Plz login again!")
            print("------------------------------------------------")


    def user_login(self):
        print("Login Page")
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in user_database:
            if password in user_database.values():
                print("Login Successful\n")
            elif password not in user_database.values():
                print("Wrong password")
        elif username not in user_database:
            print("Please create account!")
            print("------------------------------------------------")


u = User()
print("register")
#u.user_register()

print()
#u.user_login()

class Admin:
    global user_database
    user_database = {}
    username = 'admin'
    password = 123

    user_database[username] = password

    def login(self):
        username = input("Enter username: ")
        password = int(input("Enter password: "))
        print(user_database)
        if username in user_database.keys():
            if password in user_database.values():
                print("Successful\n")
                print("you are login admin account!")
            elif password not in user_database.values():
                print("Wrong password")

        elif username not in user_database.keys():
            print("Wrong username!")


a = Admin()

a.login()