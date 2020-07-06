def adding_report():
    items = ""
    total = 0
    while True:
        x = input("Enter integer or \"Q\" to quit: ")
        if x.isdigit():
            if x.lower() == 'a':
                items += x + '\n'
                total += int(x)
                print(x)
            elif x.lower() == 'q':
                print("items\n",items)
                print("total:" , total)
                break
        elif x.isdigit():
            if x.lower() == 't':
                items += x + '\n'
                total += int(x)
                print(x)
            elif x.lower() == 'q':
                print("total:" , total)

type = adding_report()
while True:
    if type == 'a':
        break
