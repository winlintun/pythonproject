shopping_dict = {}

print("Welcome to Mg Chat's fruit shop!")
print("***************************************")

user = input("Enter name: ")

while user != 'OFF':
    item = input("Enter items: ")
    quality = int(input("Enter quality: "))

    if user not in shopping_dict:

        shopping_dict[user] = {}

    if item in shopping_dict[user]:

        shopping_dict[user][item]+= quality

    else:
        shopping_dict[user][item] = quality

    user = input("Enter name: ")


print(shopping_dict)

#loop
for user in shopping_dict:
    print(user)
    for item,quality in shopping_dict[user].items():
        print('{}: {}'.format(item,quality))
    print("**************************************")