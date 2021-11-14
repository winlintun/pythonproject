weathear = 'Raining'
day = 'Sunday'
if weathear == 'Raining' and day == 'Sunday':
    print("Sleep at home")
else:
    print('no today')

number = int(input("Please enter a number: "))
if number < 0:
    number = - number
    print("Absolute number is: {}".format((number)))


age_above_20 = True
male = True
health_fitness_ok = True
if age_above_20 and male and health_fitness_ok:
    print('Serve army for two years')

user = int(input("Enter the number: "))

if user % 2 == 0:
    print(user,'is even number')
else:
    print(user, 'is odd number')

chair = str(input("Please enter a character: "))
vowel = ['a', 'e', 'i', 'o', 'A', 'E', 'I', 'O', 'U']

if chair in vowel:
    print("Input chapter is vowel")
else:
    print("input character is consonant.")


# leap year
year = int(input("Please enter Year: "))
if year % 100 != 0 and year % 4 == 0:
    print('Leap Year')
elif year % 100 == 0 and year % 400 == 0:
    print('leap year')
else:
    print('not leap year')






