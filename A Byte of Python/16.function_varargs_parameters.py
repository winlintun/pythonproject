def total(initial=5, *number, **keywords):
    count = initial
    for number in number:
        count += number

    for key in keywords:
        count += keywords[key]

    return count

print(total(10,1,2,3, vegatables=50, fruits=100))