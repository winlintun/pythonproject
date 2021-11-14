print("****ConverterProgarm****")
print('1.lenght')
print('2.weight')
print('3.temperature')
print()
print("Press 'e' for Exit!")
print()
user_input=input("Choose your option:")

while user_input != 'e':
    if user_input=='1':
        print('1.km to mile')
        print('2.mile to km')
        user_input=input("Choose your option:")
        if user_input=='1':
            form_value=int(input('Enter kilometer:'))
            to_value=form_value/1.6
            print(form_value, 'km = ', to_value, 'mile')
        elif user_input=='2':
            form_value = int(input('Enter mile:'))
            to_value = form_value * 1.6
            print(form_value,'mile = ',to_value,'km')
        else:
            print('Wrong Number!')

    elif user_input=='2':
        print('1.kg to Pound')
        print('2.Pound to kg')
        user_input=input('Choose your option:')
        if user_input=='1':
            form_value = int(input('Enter Kilogrem:'))
            to_value = form_value * 2.2
            print(form_value, 'kg = ', to_value, 'pound')
        elif user_input=='2':
            form_value = int(input('Enter Pound:'))
            to_value = form_value / 2.2
            print(form_value, 'pound = ', to_value, 'kg')
        else:
            print('Wrong Number!')
    elif user_input=='3':
        print('1.Cel to Fah')
        print('2.Fah  to Cel')
        user_input = input('Choose your option:')
        if user_input=='1':
            form_value = int(input('Enter Cel:'))
            to_value = form_value * 9/5 + 32
            print(form_value, 'Cel = ', to_value, 'Fah')
        elif user_input=='2':
            form_value = int(input('Enter Fah:'))
            to_value = (form_value - 32) + 5/9
            print(form_value, 'Fah = ', to_value, 'Cel')
        else:
            print('Wrong Number!')

    else:
        print("Wrong!")
    print("xxxxxxxxxxxxxxxxxxxxxxx")
    print()
    print()
    print("****ConverterProgarm****")
    print('1.lenght')
    print('2.weight')
    print('3.temperature')
    print()
    print("Press 'e' for Exit!")
    print()
    user_input = input("Choose your option:")