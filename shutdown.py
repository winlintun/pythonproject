import os

print("****Shutdown Computer****")
print('1.Now')
print('2.One Hour')
print('3.Two Hour')
print('4.Three Hour')
print('5.Restart')
print('6.Cancel Shutdown or Restart')
print('7.Sleep Now')
print('8.custom shutdown')
print("Press 'e' to exit!")
user_input = input("Choose your option:")

while user_input != 'e':
    if user_input == '1':
        os.system("shutdown /s /t 0")
        os.system("msg * Your Computer are Shutdown")


    elif user_input == '2':
        os.system("shutdown /s /t 3600")
        os.system("msg * Your Computer are shutdwon One Hour.")
    elif user_input == '3':
        os.system("shutdown /s /t 7200")
        os.system("msg * Your Computer are shutdwon Two Hours.")
    elif user_input == '4':
        os.system("shutdown /s /t 14400")
        os.system("msg * Your Computer are shutdwon Three Hours.")
    elif user_input == '5':
        os.system("shutdown /r /t 1")
        os.system("msg * Your Computer are Restart.")
    elif user_input == '6':
        os.system("shutdown /a")
        os.system("msg * Your Computer are Cancel now.")
    elif user_input == '7':
        os.system(("rundll32.exe powrprof.dll, SetSuspendState Sleep"))
        os.system("msg * Your Computer are sleep.")
    elif user_input == '8':
        time = input("Enter a second: ")
        os.system('shutdown /s /t {}'.format(time))
    else:
        print("Wrong Number!")
        print("Please Try Again!")
    print(">>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<")
    print()
    print()

    print("****Shutdown Computer****")
    print('1.Now')
    print('2.One Hour')
    print('3.Two Hour')
    print('4.Three Hour')
    print('5.Restart')
    print('6.Cancel Shutdown or Restart')
    print('7.Sleep Now')
    print('8.custom shutdown')
    print("Press 'e' to exit!")
    user_input = input("Choose your option:")
os.system("msg * Created by 'iceface'. Thank U!")