number = 23
running = True

while running:
    guess = int(input("Enter an integer: "))

    if guess == number:
        print("Congratulation, you guessed it.")
        # this causes the while loop to stop
        running = False

    elif guess < number:
        print("No, it is a little higher than thant.")

    else:
        print("No, it si a little lower than tha.")
        # do anything else you want to do here
print("Done")