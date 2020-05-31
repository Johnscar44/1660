


time = 3

while True:
    print('time is', time)
    if time == 3:
        time = 4
    else:
        break

x = 0

while True:
    if x < 10:
        print('run forever')
        x += 1
    else:
        break



num_1 = ""
num_temp = ""
num_final = ""

while True:
    num_1 = input("Enter an integer: ")
    if num_1.isdigit():
        num_final = num_temp + num_1
        num_temp = num_final
    else:
        print(num_final)
        break








shirt_amount = 0
s = 0
m = 0
l = 0
amount = 10


while True:
    shirt_size = input("What size?\n type s/m/l\n [e] to exit: ")

    if shirt_size.lower().startswith("e"):
        print()
        break
    elif shirt_size.lower() == "s":
        s += 1
    elif shirt_size .lower()== "m":
        m += 1
    elif shirt_size.lower() == "l":
        l += 1
    else:
        print("invalid entry counted as medium")
        m += 1
    shirt_amount += 1
    if shirt_amount >= amount:
        print("no more shirts left")
        break
print(shirt_amount , "total:" , s , "small shirts" , m , "medium shirts" , l , "large shirts")
