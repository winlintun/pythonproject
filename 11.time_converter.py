#This is comment
"""
This is comment

"""
seconds_in_minute=60
seconds_in_hour=3600


seconds=int(input("Enter seconds: "))

#converting hour from seconds
hour = seconds // 3600
#printing hour
if hour!=0:
    if hour==1:
        print(hour,'hour',end=' ')
    else:
        print(hour,'hours',end=' ')


#remaing seconds after the hours are sccounted for
seconds = seconds%3600

#converting minutes from remaing seconds after the hours are accounted for
mintues =seconds // 60

#printing mintues
if mintues!=0:
    if hour==1:
        print(mintues,'mintue',end=' ')
    else:
        print(mintues,'mintues',end=' ')


#reamining seconds after the minutes are accounted for
seconds = seconds % 60
#printing seconds
if seconds!=0:
    if seconds==1:
        print(seconds,'second',end=' ')
    else:
        print(seconds,'seocnds',end=' ')

print()
print()

print(hour,'hours',mintues,'mintues',seconds,'seconds')



