import os

class Shutdown:

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def hour_to_second(self):
        second = self.hour * 3600
        print('{} hours to {} second'.format(self.hour, second))
        return second

    def minute_to_seocnd(self):
        second = self.minute * 60
        print(second)
        print('{} minute to {} second'.format(self.minute, second))
        return second


def menu():
    print("********Welcome to shutdwon program**********")
    print("""
    1. Hours
    2. Minutes
    3. Cancel Shutdown
    4. Exit Program! press '4'.
    """)

menu()

user = int(input("Enter fist step number: "))

#user = int(input("Enter while loop: "))

while user != 4:
    if user == 1:
        a = input("Enter hour: ")
        try:
            a = int(a)
            b = 2
            s = Shutdown(hour=a, minute=b)
            shutdown = s.hour_to_second()
            os.system("shutdown /s /t {}".format(shutdown))

        except ValueError:
            print("Wrong Hour Number!!!")
            print()

    elif user == 2:
        b = input("Enter minute: ")
        try:
            b = int(b)
            a = 1
            s = Shutdown(hour=a, minute=b)
            shutdown = s.minute_to_seocnd()
            os.system("shutdown /s /t {}".format(shutdown))

        except ValueError:
            print("Wrong Minute Number!!!")
            print()

    elif user == 3:
        os.system("shutdown /a")
        print("Your computer are now cancel.")
        #os.system("msg * Your Computer are Cancel now.")

    elif user == 4:
        print('exiting!!!')
        exit()

    else:
        print("Wrong Number")

    menu()
    user = int(input("Enter finish step number: "))

exit()

# erro အဆင်ပြေသွားပီ


''' 
ပထမဆုံး ဘာလဲဆိုတော့ error ဖမ်းတာပါ tryနက် ဖမ်းပါတယ် အဆင်မပြေလို စမ်းနေတာ ကြာပါပီ
အခုက အောက်ဆုံး input function ကို tab တစ်ချက် ခုန်လိုက်ရင် အဆင်ပြေသွားတယ် ဟီး/./////

ok 
အစက ကြိုက်တဲ့ နာရီ ရယ် မိနစ်တွေ နက် ကွန်ပျူတာကို ပိတ်စေချင်တာပေါ့
နာရီကနေ စက္ကန့် ပြောင်းတာပေါ့
မိနစ် ကနေ စက္ကန့် ပြောင်းတာပေါ့

ပီးတော့ while loop နက် infinity loop ပတ်တယ်
ပီးတော့ if loop နက် ဘယ်number ထည့်ရင် ဘာလုပ်မယ်ဆိုပီး ပတ်တယ်

ပီးတော့ အကယ်ပေါ့ user က 1 ထည့်လိုက်ရင် နာရီပေါ့ ပီးတော့ user က number ထည့်ရင် ပြသနာ မတက်ဘူး
ဒါပေမယ့် ပေါက်ကရ ဂဏန်းထည့်ရင် erro ဖမ်းမပေးဘူး အဲ့တော့ try except နက် ဖမ်းတယ်
number only ကလွဲရင် value Error တက်မယ်ဆိုပီးတော့ပေါ့

အခုတော့ အဆင်ပြေသွာ့ပီ

ဒီ program မှာ အားနည်းချက် ရှိတာ သိပါတယ် ဒီထက်မက ကောင်းအောင် ပိုမြန်အောင် ရေးလို့ ရသေးတာ သိပါတယ်
လိုလိုဆယ်မှာတော့ ကိုယ်က အဲ့ထိတော့ မရသေးဘူး 

ပထမဆုံး ရေးထားတဲ့ ဒိဟာကိုပဲ ပြမယ်နော်


'''