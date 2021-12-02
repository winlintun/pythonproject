class User:
    global user_database

    user_database = {} # empty dictionary

    def __init__(self):
        pass

    def user_register(self):
        print("""
 ------------------------------------------------------
 |======================================================| 
 |============= Welcome Register System ================|
 |======================================================|
  ------------------------------------------------------""")
        try:
            username = input("Enter username: ")
            password = int(input("Enter password: "))
        except:
            print("Wrong username and password")
            print("Please retry again")
            user_register(self)

        if username not in user_database:
            user_database[username] = password
            print("Create account is successful")
            print(f">>>Your account<<<\n username:{username}\n password:{password}\n")
            print("------------------------------------------------")
        elif username in user_database:
            print("Your {} account is exist!".format(username))
            print("Plz login again!")
            print("------------------------------------------------")

    def search_product(self):
        print("Search Product")
        my_list = ['apple', 'banana', 'ogrange', 'pinkapple', 'strawberry']
        for i in my_list:
            print(i,end=', ')

    def view_product(self):
        print("View Product")

    def buy_and_add_to_card(self):
        user_input = input("Do you have payment: (Y/N): ")
        if user_input == 'Y' or user_input == 'y':
            print("Payment System")
            print("1: Online Payment \n2: Cash on Delivery\n3: Exiting Payment :")
            choose = int(input("Enter option: "))

            if choose == 1:
                print("Online Payment")
                print("Payment Successful!\n Order Placed")

            elif choose == 2:
                print("Cash on Delivery")
                print("Payment Successful\n Order Placed")
            elif choose == 3:
                print("Exiting....")
        
        elif user_input == 'N' or user_input =='n':
            return buy_and_add_to_card(self)

    def order_place(self):
        print("Order Placed.")


    def user_login(self):
        print("""
 ------------------------------------------------------
 |======================================================| 
 |============== Welcome Login System ==================|
 |======================================================|
  ------------------------------------------------------""")
        username = input("Enter username: ")
        password = int(input("Enter password: "))

        if username in user_database:
            if password in user_database.values():
                print("Login Successful\n")
                print("""
                    1. Search Product
                    2. View Product
                    3. Buy and add to card
                    4. Order Place
                    5. Logout
                    """)
                see = int(input("Enter options: "))
                
                if see == 1:
                    return User.search_product(User)
                elif see == 2:
                    return User.view_product(User)
                elif see == 3:
                    return User.buy_and_add_to_card(User)
                elif see == 4:
                    return User.order_place(User)
                else:
                    print("Logout {} name".format(username))


            elif password not in user_database.values():
                print("Wrong password")
        elif username not in user_database:
            print("Please create account!")
            print("------------------------------------------------")

class Admin:
    global user_database
    user_database = {}
    username = 'admin'
    password = 123

    user_database[username] = password

    def login(self):
        print("Admin Login Page")
        username = input("Enter username: ")
        password = int(input("Enter password: "))
        #print(user_database)
        if username in user_database.keys():
            if password in user_database.values():
                print("Successful\n")
                print("you are login admin account!")

            elif password not in user_database.values():
                print("Wrong password")
                print("------------------------------------------------")

        elif username not in user_database.keys():
            print("Wrong username!")
            print("------------------------------------------------")

class Gust:
    global user_database

    user_database = {} # empty dictionary
    username = 'gust'
    password = '123'
    user_database[username]=password

    def gust(self):
        print("Gust Account")
        if 'gust' in user_database:
            print("Login Successful\n")
            print("""
                1. Search Product
                2. View Product
                3. Logout
                """)
            see = int(input("Enter options: "))
            
            if see == 1:
                return User.search_product(User)
            elif see == 2:
                return User.view_product(User)
            else:
                print("Exiting.......")



class Start:
    """docstring for Start"""
    def __init__(self):
        pass

    def first(self):
        choose = int(input("""
            1: User 
            2: Admin
            3: Gust Account
            4: Exiting Program :"""))

        if choose == 1:
            print("Welcome User Login Page\n")
            print("Login or Register")

            try:
                choose = int(input("Enter (\n1: Register\n2: Login) :"))
            except ValueError:
                print("Wrong Enter Number!")
                choose = int(input("Enter (1: User / 2: Admin) :"))

            if choose == 1:
                User.user_register(Start)
                
            elif choose == 2:
                User.user_login(Start)
            else:
                print("Wrong options!")


        elif choose == 2:
            print("Welcome Admin Login Page")
            Admin.login(Start)

        elif choose == 3:
            print("Gust Default Account")
            Gust.gust(Start)
        else:
            print("Exiting Program")
            exit()
            

bye = "\n Exiting Program! \n Thank You \n "

def runagin():
    a= Start()
    a.first()

    try:
        run = str(input("\nWant to run again: (y/n): "))

    except:
        print("Please yes or no!")

    if run == 'y' or run == 'Y':
        a.first()
        runagin()
    elif run == 'n' or run == 'N':
        quit(bye)


runagin()