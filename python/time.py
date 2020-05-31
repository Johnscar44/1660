import time
import threading


print("start time")
start_time = time.time()
print(start_time)
stoppper = input("press enter to stop")
end_time = time.time()
print("You have finished")
print(end_time)
print ("--------------------")
duration = int(end_time - start_time)
print(duration)
while True:
    if duration > 3:
        print("Bad Luck You Were Not Fast Enough")
        break
    else:
        print("Well Done You Are Very Quick! :) ")
        break



import threading
def mytimer():
   print("Python Program\n")
my_timer = threading.Timer(3.0, mytimer)
my_timer.start()
print("Cancelling timer\n")
my_timer.cancel()
print("Bye\n")
