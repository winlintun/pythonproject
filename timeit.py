from datetime import datetime


start = datetime.now()


a = 0 
for i in range(1000):
	a += (i**100)


end = datetime.now()


print("The time of execution of avobe program is: ", str(end-start)[5:])


