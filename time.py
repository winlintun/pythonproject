import time

# starting time
start = time.time()


# program

def sum(n):
	
	final_sum = 0 

	for x in range(n+1):
		final_sum += x 

	return final_sum

print(sum(5))



end = time.time()

# total time taken

print("Runtime of the program is: ", end - start)


# starting time
start = time.time()


# program

def sum1(n):
	return (n*(n+1))/2


print(sum1(5))



end = time.time()

# total time taken

print("Runtime of the program is: ", end - start)