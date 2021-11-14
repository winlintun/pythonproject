import random
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')

#computer_guess(5)
a = 'b'
user = input(f"a number is {a} high (apple), low (ball), or correct (cut):  ").lower()

if user in a:
    print("yes")
elif user not in a:
    print("no")
else:
    print("correct")

