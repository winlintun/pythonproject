while True:
    a = input("Enter something: ")
    if a == 'quit':
        break
    if len(a) < 3:
        print("Too small")
        continue
    print("input is of sufficient leight")
