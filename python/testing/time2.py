import time
def timer():
    sec = 0
    min = 0
    while True:
        sec += 1
        time.sleep(1)
        if sec == 60:
            sec = 0
            min += 1
        elif sec >= 60:
            return True


kill = timer()
while True:
    x = input("talk to me for 60 seconds: ")
    if kill == True:
        print("i suck at making conversation")
    elif kill == False:
        print("your boring bye")
        break
