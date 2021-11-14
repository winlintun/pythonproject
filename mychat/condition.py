mark = int(input("Enter your mark = "))

if mark >= 70:
    grade = 'C'
elif mark >=80:
    grade = 'B'
elif mark >= 90:
    grade = 'A'
else:
    grade = 'D'
print("you grade is",grade)
