def get_recursive_factorial(n):
    if n < 0:
        return -1
    elif n < 2:
        return 1
    else:
        return n * get_recursive_factorial(n-1)

print(get_recursive_factorial(2))

# correct this code for loop
def get_iterative_factorial(n):
    if n < 0:
        return -1
    else:
        fact = 1
        for i in range(1, n+1):
            fact *= i

        return fact

print(get_iterative_factorial(34))

for j in range(1, 6): print(j)

print("""

>>>>>factorial formula = n * factorial(n-1)<<<<
1 > fact * i > 1 *  1 = 1
2 > fact * i > 1 * 2 = 2
3 > fact * i > 2 * 3 = 6
4 > fact * i > 6 * 4 = 24
5 > fact * i > 24 * 5 = 120

""")

