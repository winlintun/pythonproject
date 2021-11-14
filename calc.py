num1 = input("Enter First Number: ")
num2 = input("Enter Second number: ")
op = input("Choose +, -, *, / : ")

while op != 'e':


    try:
        num1 = int(num1)
        num2 = int(num2)
        output = True
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2

        else:
            output = False
            print("Wrong Operator!")
            print("Try Again!")
            print()
            print()
        if output:
            print("Your Result is = ", result)
        user_input = input("Enter 'e' for exit & 'enter' for continue :  ")
        if user_input == 'e':
            user_input = exit()
        else:
            print("Thank U!")
    except ValueError:
        print("Please Try Number Only!")
    print()
    print()
    num1 = input("Enter First Number: ")
    num2 = input("Enter Second number: ")
    op = input("Choose +, -, *, / : ")