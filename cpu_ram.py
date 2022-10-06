import psutil 
import datetime
# calling psutil.cpu_percent() for 4 second

start = datetime.datetime.now()

print('The CPU usage is: ', psutil.cpu_percent(4))

end = datetime.datetime.now()

print("Run time: ", end - start)
import os
import psutil
 
start = datetime.datetime.now()

# Getting loadover15 minutes
load1, load5, load15 = psutil.getloadavg()
  
cpu_usage = (load15/os.cpu_count()) * 100
  
print("The CPU usage is : ", cpu_usage)

end = datetime.datetime.now()
print("Run time: ", end - start)