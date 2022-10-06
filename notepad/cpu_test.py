import psutil 
import datetime
# calling psutil.cpu_percent() for 4 second

# start = datetime.datetime.now()

while True:
	try:
		print('The CPU usage is: ', psutil.cpu_percent(1))
	except (KeyboardInterrupt, Exception) as error:
		print(error)
		break



