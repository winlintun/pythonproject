number = 23
guess = int(input("Enter an integer: "))

if guess == number:
    # new block starts here
    print("Congratulations,you guessed it.")
    print("but you do not with any prizes!")
elif guess < number:
    # another block
    print("No, it is a little highter than that")
    # you can do whatever you want in a block
else:
    print("No, it is a little lower than that")
    #you must have gussed > number to reach here

print("Done")
# this last statement is alway executed
# after the if statement is executec.
