def get_report_type():
    while True:
        type = input("what report do you want: ")
        if do_exit(type):
            return False
        if type.isalpha():
            if type.lower() == 'a':
                print(type)
                return type
            elif type.lower() == 't':
                print(type)
                return type
            else:
                print("incorrect")
                continue

def add():
    items = ""
    total = 0
    while True:
        num = input("enter int \nor\ndone for items and total\n[q] to quit: ")
        if do_exit(num):
            return False
            if num.isdigit():
                items += num + '\n'
                total += int(num)
                print(num)
            elif num == "done".lower():
                return items
                return total
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
    num = add()
    if num == False:
        print("gooodbye")
        break
        if num == True:
            x += num + '\n'
            y += int(num)
            print(num)
            print(x)
            print(y)
