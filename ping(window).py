import os

print("Ping Service")
print("Internet checking with ping")
print()
print("1.Ping www.google.com")
print("2.Ping www.youtube.com")
print("3.Ping www.facebook.com")
print("4.Ping Local Network")
print("5.Check Your Ip Address")
print()
print("Press 'e' for Exit!")


import socket
host = socket.getfqdn()
addr = socket.gethostbyname(host)

#print(f"Your ip is {addr}")
# On Linux, it may give you the localhost address

user_input = input("Choose Options: ")

print()
print()
while user_input != 'e':

    if user_input == '1':
        os.system("ping 8.8.8.8")
        print("You Connection is Good")
    elif user_input == '2':
        os.system("ping 74.125.24.136")
        print("You Connection is Good")
    elif user_input == '3':
        os.system("ping 157.240.7.35")
        print("You Connection is Good")
    elif user_input == '4':
        os.system(f"ping {addr}")
        print("You Connection is Good")
    elif user_input == '5':
        print(f"You ip address is : {addr}")

    else:
        print("Wrong Number!")
        print("You Connection is Down!")


    print("Thank You!")
    print()
    print()
    print("Ping Service")
    print("Internet checking with ping")
    print()
    print("1.Ping www.google.com")
    print("2.Ping www.youtube.com")
    print("3.Ping www.facebook.com")
    print("4.Ping Local Network")
    print("5.Check Your Ip Address")
    print()
    print("Press 'e' for Exit!")

    user_input = input("Choose Options: ")
print("Thank You!")