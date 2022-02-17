# import os

# class Shutdown:

#     def __init__(self, hour, minute):
#         self.hour = hour
#         self.minute = minute

#     def hour_to_second(self, second):
#         second = self.hour * 3600
#         print('{} hours to {} second'.format(self.hour, second))
#         return second

#     def minute_to_seocnd(self, minute):
#         minute = self.minute * 60
#         print(minute)
#         print('{} minute to {} second'.format(self.minute, minute))
#         return minute


# def menu():
#     print("********Welcome to shutdwon program**********")
#     print("""
#     1. Hours
#     2. Minutes
#     3. Cancel Shutdown
#     4. Exit Program! press '4'.
#     """)

# menu()

# user = int(input("Enter fist step number: "))

# #user = int(input("Enter while loop: "))

# while user != 4:
#     if user == 1:
#         a = input("Enter hour: ")
#         try:
#             a = int(a)
#             b = 2
#             s = Shutdown(hour=a, minute=b)
#             shutdown = s.hour_to_second()
#             os.system("shutdown /s /t {}".format(shutdown))

#         except ValueError:
#             print("Wrong Hour Number!!!")
#             print()

#     elif user == 2:
#         b = input("Enter minute: ")
#         try:
#             b = int(b)
#             a = 1
#             s = Shutdown(hour=a, minute=b)
#             shutdown = s.minute_to_seocnd()
#             os.system("shutdown /s /t {}".format(shutdown))

#         except ValueError:
#             print("Wrong Minute Number!!!")
#             print()

#     elif user == 3:
#         os.system("shutdown /a")
#         print("Your computer are now cancel.")
#         #os.system("msg * Your Computer are Cancel now.")

#     elif user == 4:
#         print('exiting!!!')
#         exit()

#     else:
#         print("Wrong Number")

#     menu()
#     user = int(input("Enter finish step number: "))

# exit()
# from datetime import datetime
# import time
# import os

# class Shutdown:

#     def __init__(self) -> None:
#         pass

    
#     def hour_to_second(self, hour):
#         try:
#             hour_second = hour * 3600
#             print('hours: ', self.hour)
#             os.system('shutdown /s /t {}'.format(hour_second))
#         except (Exception, os.error) as e:
#             print(e)

#     def minute_to_second(self, minute):
#         try:
#             minute_second = minute * 60
#             print("minutes: ", self.minute)
#             os.system('shutdown /s /t {}'.format(minute_second))
#         except (Exception, os.error) as e:
#             print(e)

#     def cancel_program(self):
#         try:
#             os.system('shutdown /a')
#         except (Exception, os.error) as e:
#             print(e)
    


#     def start(self):
#         now = datetime.now()
#         print("\nProgram loading...")
#         for i in range(5):
#             print('. ', end='')
#             time.sleep(1)
        
#         print(f"""
#         {now}
#         \n-----------------------------------------------
#                 Welcome Windows Shutdown Program
#         -----------------------------------------------
#         1. hour
#         2. minute
#         3. cancel
#         4. exit\n
#         """)
#         user = int(input("Enter Options: "))
        
#         while True:
#             if user == 1:
#                 hour = input('Enter hours: ')
#                 self.hour_to_second(hour)
#                 user = int(input("Enter Options: "))
#             elif user == 2:
#                 minute = input("Enter minute: ")
#                 self.minute_to_second(minute)
#                 user = int(input("Enter Options: "))
#             elif user == 3:
#                 self.cancel_program()
#                 user = int(input("Enter Options: "))
#             else:
#                 print("Exiting Program")
#                 for i in range(5):
#                     print('.', end=' ')
#                     time.sleep(1)
#                 if user is not None:
#                     os.system('cls')
#                 else:
#                     os.system('clear')
#                 break
                        




# if __name__ == '__main__':
#     shutdown = Shutdown()
#     shutdown.start()



from ast import While
from datetime import datetime
import time
import os
import platform
my_os = platform.system()

def hour_to_second(hour):
    hour_second = hour * 3600
    print(hour, " hours")
    return hour_second

def minute_to_second(minute):
    minute_second = minute * 60
    print(minute, ' minutes')
    return minute_second

def cancel_program():
    os.system("system /a")
    print('You shutdown program are cancel now!!!')


def detect_os_cls_screen():
    if my_os == 'Windows':
        os.system("cls")
    else:
        os.system("clear")

def menu():
    print("""
        -----------------------------------------------
                Welcome Windows Shutdown Program
        -----------------------------------------------
        1. Shutdown Now
        2. Restart
        3. Sleep Now
        ------------------- or --------------------------
        4. hour
        5. minute
        6. cancel
        7. exit\n
        """)

def start():
    detect_os_cls_screen()

    wel = 'Program Loading....\n'
    for i in wel:
        print(i, end=' ')

    menu()
    try:
        user = int(input("Enter Options: "))
    except (Exception, ValueError) as e:
        print(e)

    while True:
        if user == 1:
            try:
                os.system("shutdown /s /f")
            except (Exception, os.error) as e:
                print(e)
            finally:
                # detect_os_cls_screen()
                menu()
                try:
                    user = int(input("Enter Options: "))
                except (Exception, os.error) as e:
                    print(e)

        elif user == 2:
            try:
                os.system("shutdown /r /f")
            except (Exception, os.error) as e:
                print(e)
            finally:
                # detect_os_cls_screen()
                menu()
                try:
                    user = int(input("Enter Options: "))
                except (Exception, os.error) as e:
                    print(e)

        elif user == 3:
            try:
                os.system(("rundll32.exe powrprof.dll, SetSuspendState Sleep"))
            except (Exception, os.error) as e:
                print(e)
            finally:
                # detect_os_cls_screen()
                menu()
                try:
                    user = int(input("Enter Options: "))
                except (Exception, os.error) as e:
                    print(e)

        elif user == 4:
            try:
                user_hour = int(input("Enter hours: "))
                hour = hour_to_second(user_hour)
                os.system("shutdown /s /t {}".format(hour))
            except (Exception, os.error) as e:
                print(e)
            finally:
                # detect_os_cls_screen()
                menu()
                try:
                    user = int(input("Enter Options: "))
                except (Exception, os.error) as e:
                    print(e)

        elif user == 5:
            try:
                user_minute = int(input("Enter minutes: "))
                minute = minute_to_second(user_minute)
                os.system("shutdown /s /t {}".format(minute))
            except (Exception, os.error) as e:
                print(e)
            finally:
                # detect_os_cls_screen()
                menu()
                try:
                    user = int(input("Enter Options: "))
                except (Exception, os.error) as e:
                    print(e)
                    
        elif user == 6:
            try:
                os.system("shutdown /a")
            except (Exception, os.error) as e:
                print(e)
            finally:
                # detect_os_cls_screen()
                menu()
                user = int(input("Enter Options: "))
                
        else:
            bye = 'Thank U!!!'
            for i in bye:
                print(i)
                time.sleep(1)
            exit(bye)

if __name__ == '__main__':
    start()