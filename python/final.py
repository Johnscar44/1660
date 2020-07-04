print("")
print("")
print("\twelcome to my adding report program!".title())
print("\tit's been made a little differently.".title())
print("")
print("I've made a done command, so you can make mulitible lists\n\t     and you can quit at anytime!")
print("")
print("")

def get_report_type():
    while True:
        type = input("what report would you like?\n[A] for all items and total\n[T] for just the total\n[Q] to quit at anytime: ")
        if do_exit(type):
            return False
        if type.isalpha():
            if type.lower() == 'a':
                return type
            elif type.lower() == 't':
                return type
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
        else:
            ("invalid entry! try again")
            return None

def do_exit(data):
    if data.isalpha():
        if data.lower() == 'q':
            return True
    else:
        return False


data = get_report_type()
while True:
    if data == False:
        print("goodbye")
        break
    elif data == 'a':
        add()
    elif data == 't':
        total()
    num = add()
    if num == False:
        print("gooodbye")
        break
    if data == 'a':
        add()
    if data == 't':
        total()
