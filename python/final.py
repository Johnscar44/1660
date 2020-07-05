def adding_report():
    while True:
        type = input("choose report type (\"A\" or \"T\")\nreport types include all items (\"A\") or total only (\"T\")".title())
        if type.isalpha():
            if type.lower() == 'a':
                return type
            elif type.lower() == 't':
                return type
<<<<<<< HEAD
            else:
                print("incorrect")
                continue

def total():
    items = ""
    total = 0
    print("T selected")
    print("enter int!")
    while True:
        tot = input("enter int: ")
        if do_exit(tot):
            return False
            if tot.isdigit():
                items += tot + '\n'
                total += int(tot)
                print(tot)
            elif tot == "Done".lower():
                print("")
                print("total:" , total)
                print("")
                print("")
            else:
                ("invalid entry! try again")
                return None

def add():
    items = ""
    total = 0
    print("A selected")
    while True:
        num = input("enter int!: ")
        if do_exit(num):
            return False
            if num.isdigit():
                items += num + '\n'
                total += int(num)
                print(num)
            elif num == "Done".lower():
                print("")
                print("items\n",items)
                print("total:" , total)
=======
            elif type.lower().startswith('q'):
                return type
>>>>>>> 6b5f8f75ddcb1479e86942d206328d2db8d8de3e
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
