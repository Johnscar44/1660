import time

print("welcome to my gun game!\nyou have 30 rounds in your gun use them up!\nyou also have health for a different ending".title())
print("intructions.. \ninputs are!")
print("pulltrigger\nholdtrigger\n")
print("pulltrigger shoots once \nholdtigger shoots 10 times")
print("type [exit] or [e] to leave the game")

times_shot = 0
total_rounds = 30
total_health = 100
sec = 0
min = 0


def timer_chal():
print("This is the timer")
start = input("Would you like to begin Timing? (y/n): ")
if start == "y":
    timeLoop = True
sec = 0
min = 0
timeLoop = start
while timeLoop:
    sec += 1
    time.sleep(1)
    if sec == 60:
        sec = 0
        min += 1
    return min
    return sec

while True:
    click = input("shoot the gun!: ".title())
    if click.lower().startswith("e"):
        print("we shot you in the back!\nyour dead now.. lol".title())
        break
    elif click == "pulltrigger".lower():
        times_shot += 1
        print("bang!".upper())
    elif click == "holdtrigger".lower():
        times_shot += 10
        print("bang\n" * 10)
    else:
        print('that is not a command! We shot you!')
        total_health -= 20
    times_shot += 1
    if total_rounds < times_shot:
        print("congrats!! you are now wanted for the murder of mulitiple people!".title())
        print("thanks for playing scumbag!".title())
        print(min , sec)
        break
    elif total_health <= 0:
        print("your dead... \n im not sure how this was a very easy game...")
        print("well either way my god have mercy on your soul..".title())
        print(min , sec)
        break
