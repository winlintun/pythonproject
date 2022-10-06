import tracemalloc

def app():
	lt = []

	for i in range(0, 10000):
		lt.append(i)


tracemalloc.start()


app()


print(tracemalloc.get_traced_memory())

tracemalloc.stop()