def adding_report():
    while True:
        type = input("choose report type (\"A\" or \"T\")\nreport types include all items (\"A\") or total only (\"T\")".title())
        if type.isalpha():
            if type.lower() == 'a':
                return type
            elif type.lower() == 't':
                return type
            elif type.lower().startswith('q'):
                return type
        else:
            print("incorrect")



data = adding_report()
items = ""
total = 0
while True:
    x = input("Enter integer or \"Q\" to quit: ")
    if data == "a":
        if x.isdigit():
            items += x + '\n'
            total += int(x)
        elif x == "q":
            print("items\n",items)
            print("total:",total)
            break
        else:
            print(x , "is invalid input")
    if data == "t":
        if x.isdigit():
            items += x + '\n'
            total += int(x)
        elif x == "q":
            print("total:",total)
            break
        else:
            print(x , "is invalid input")
