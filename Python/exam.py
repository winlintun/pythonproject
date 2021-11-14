number_of_sub = int(input("Enter number of subject: "))


pass_mark = 40
is_pass = True

for i in range(number_of_sub):
    mark = float(input("Enter marks for subject: "+ str(i)))
    is_pass = is_pass and i >= 40

if is_pass:
    print("Pass the exam")

else:
    print("Fail the exam")
