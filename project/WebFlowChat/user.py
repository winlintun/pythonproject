def menu():
    print("""
    1. Register
    2. Login
    3. Gust Account""")


user_database = {}


def Register():
    print("\n<<<<<<<<<<<Welcome Register From<<<<<<<<<<<")
    try:
        username = str(input("Enter username: "))
        password = int(input("Enter password: "))
        if username not in user_database.values():
            user_database[username] = password
            print("Successful\n")
            print("Welcome New User \n Your new account\n username: {}\n password: {}".format(username, password))
        else:
            print("Your account is already in database!")
    except ValueError:
        print("username is chapter and password is integer")
    return run_again()


def Login():
    print("\n<<<<<<<<<<<Welcome Login From<<<<<<<<<<<")
    try:
        username = str(input("Enter username: "))
        password = int(input("Enter password: "))
        if username in user_database.keys():
            if password in user_database.values():
                print("Successful Login\n")
                pass # see product list and chose
        elif username not in user_database.keys():
            print("Your account name {} not in my database.".format(username))
            print("Try again!")
            pass # got to register from or exit
        elif username in user_database.keys():
            if password not in user_database.values():
                print("Wrong Password!")
                pass # to go try agin or not
        else:
            print("Your account does not exist my database.\n Please try again!!!")
    except ValueError:
        print("username is chapter and password is integer")
    return run_again()


def Gust_Account():
    print("\n<<<<<<<<<<<Welcome Gust User<<<<<<<<<<<")
    pass
    return run_again()


def run_again():
    try:
        user_input = str(input("continue: yes or exit: no :"))
        if user_input == 'Y' or user_input == 'y' or user_input == 'yes' or user_input == 'Yes' or user_input == 'YES':
            user_login()
            run_again()
        else:
            bye = """
            |=================================|
            |======== Exiting Program ========|
            |=================================|
            """
            print(quit(bye))
    except ValueError:
        print("Please enter yes or no!!!")


def user_login():
    menu()
    option = int(input("enter option: "))
    print("\n************User Login Page************")
    if option == 1:
        Register()
    elif option == 2:
        Login()
    elif option == 3:
        Gust_Account()
    else:
        print("Wrong Options!!!!!")


if __name__ == '__main__':
    user_login()
