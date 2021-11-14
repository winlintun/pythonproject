import sys
import time

f = None
try:
    f = open("poem.txt")
    # our usual file-reading idiom
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line),sys.stdout.flush()
        print("Press Crt+c now")
        # to make suere it runs for a while
        time.sleep(2)

except IOError:
    print("Cloud not find file pome.txt")
except KeyboardInterrupt:
    print("!! you cancelled the reading from the file")
