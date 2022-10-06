from datetime import datetime 

print("""
	------------ Welcome ----------------
	1. Write or Overwrite
	2. Append Write
	3. Show Data
	""")

user = input("")

with open('notepad.txt', 'w') as file:
	user_input = str(input("Enter the data: "))
	file.write(user_input + '\n' + str(datetime.now()) + '\n')


with open('notepad.txt', 'r') as file:
	print(file.read())

