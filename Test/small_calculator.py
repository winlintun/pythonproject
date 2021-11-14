print("""
#####################################
## Simple Calculator with Forever  ##
## Loop                            ##
## Mcoder Python Tutorial          ##
##                                 ##
##                                 ##
#####################################
""")

print("""
<======Choice The Number======>
1. Calculate Number:
2. Exit Program
""")
user_input = input("Input Number: ")
while user_input != '2':


        if user_input == '1':
            print("Welcome!")
            num1 = input("Enter The First Numer: ")
            op = input("Choose operator: (+,-,*,/): ")
            num2 = input("Enter The Second Number: ")
            try:
                num1 = int(num1)
                num2 = int(num2)
                if op == '+':
                    result = num1 + num2
                    print("Answer:",num1,'+',num2,'=',result)
                elif op == '-':
                    result = num1 - num2
                    print("Answer:",num1,'-',num2,'=',result)
                elif op == '*':
                    result = num1 * num2
                    print("Answer:",num1,'*',num2,'=',result)
                elif op == '/':
                    result = num1 / num2
                    print("Answer:",num1,'/',num2,'=',result)
                else:
                    print("Please Number Only Again!")
                print("""
                <======Choice The Number======>
                1. Calculate Number:
                2. Exit Program
                """)
                user_input = input("Input Number: ")


            except ValueError:
                print("Please Enter Number Only!!")
        elif user_input == '2':
            exit()
        else:
            print("Wrong Number!")
        print("Exiting Program!.Thank You!")
        print("Good Bye!!!!")
        print()
        print()
