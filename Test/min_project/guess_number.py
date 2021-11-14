import random

def guess(x):
    guess = 0
    random_number = random.randint(1, x)

    while guess != random_number:
        guess = int(input(f"plz guees number between 1 and {x}: "))
        if guess < random_number:
            print("your number is low")
        elif guess > random_number:
            print("your number is too high")

        else:
            print("yes you anser is correct")

def compuer_guess(x):
    low = 1
    heigh = x
    feedback = ''

    while feedback != 'c':
        if low != heigh:
            guess = random.randint(low, heigh)
        else:
            guess = low

        feeback = input(f"Is {guess} high (h), low (l) or correct (c): ").lower()

        if feedback == 'h':
            high = guess - 1

        elif feedback == 'l':
            low = guess + 1
    
    print(f"the computer {guess} is correct")

guess(10)