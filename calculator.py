class Calculator:

	total = 0

	def __init__(self, x, y):
		self.x = x 
		self.y = y
		total = 0

	def sum(self):
		total =  x + y 
		return total

	def mult(self):
		total = x * y 
		return total

	def sub(self):
		total = x - y 
		return total

	def dev(self):
		total = x / y 
		return total

	def dev2(self):
		total = x // y 
		return total

	def power(self):
		print("Example x ** y = y is power")
		total = x ** y 
		return total


x = int(input("Enter first value: "))
y = int(input("Enter second value: "))
cal = Calculator(x, y)

print(cal.sum())
print(cal.sub())
print(cal.mult())
print(cal.dev())
print(cal.power())


