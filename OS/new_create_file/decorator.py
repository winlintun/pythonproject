def argument_text_natural_number(f):
	def helper(x):
		if type(x) is int and x > 0:
			return f(x)
		else:
			raise Exception("Argument is not an integer")
	return helper

@argument_text_natural_number
def factorial(n):
	if n == 1:
		return 1

	else:
		return n*factorial(n-1)

print(factorial(5))
print()

def memoize(f):
	memo = {}

	def helper(n):
		if n not in memo:
			memo[n] = f(n)
		return memo[n]
	return helper

arguments = []

@memoize
def fib(n):
	arguments.append(n)
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

print([fib(i) for i in range(5)])
