"""
number_of_sub = int(input("Enter number of subject: "))
#marks = []

pass_mark = 40
is_pass = True
for i in range(number_of_sub):
    mark = float(input("Enter marks for subject: "+ str(i)))
    is_pass = is_pass and i >= 40
    #marks.append(mark)

if is_pass:
    print("Pass the exam")

else:
    print("Fail the exam")


"""
my_list = [10,20,30,40]

for i in my_list:
    print("my list",i)
    i *= 2

for i in range(len(my_list)):
    print("Item",my_list[i])
    my_list[i] *= 2

print("my list",my_list)
