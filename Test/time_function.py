
from datetime import datetime

def date(time):



    now = datetime.now() # current date and time
    day = now.strftime("%d")
    month = now.strftime("%m")
    times = now.strftime("%H:%M:%S")
    year = now.strftime("%Y")



    if time == 1:
        print("Time: ",times)
    elif time == 2:
        print("Day: ",day)
    elif time == 3:
        print("month: ",month)
    elif time == 4:
        print("Year: ",year)
    else:
        print("Try Again")
print("""
    1. Times
    2. Day
    3. Month
    4. Year """)

user_input = int(input("Enetr number: "))
print(date(user_input))


from datetime import datetime
import pytz

print("Welcome Global Time")
print(" 1. New Your Time\n 2. London Time\n 3. Myanmar Time")

user = input("Enter the time: ")

def time(aa):
    tz_NY = pytz.timezone("America/New_York")
    datetime_NY = datetime.now(tz_NY)


    tz_London = pytz.timezone("Europe/London")
    datetime_London = datetime.now(tz_London)



    tz_Myanamr = pytz.timezone("Asia/Yangon")
    datetime_Myanmar = datetime.now(tz_Myanamr)



    if aa == '1':
        print("New York time: ",datetime_NY.strftime("%Hhr %Mmin %Ssec %p"))
    elif aa == '2':
        print("London time: ", datetime_London.strftime("%Hhr %Mmin %Ssec %p"))
    elif aa == '3':
        print("Myanmar Time: ", datetime_Myanmar.strftime("%Hhr %Mmin %Ssec %p"))
    else:
        print("Try again!")



print(time(user))
