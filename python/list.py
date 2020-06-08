items = ""
total = 0
while True:
    x = input("enter int:")
    if x:
        items += x + '\n'
        total += int(x)
        print(x)
    else:
        print("items\n",items)
        print("total:" , total)
        break
