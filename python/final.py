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
    num = input("enter int: ")
    if do_exit(num):
        return False
    if num.isdigit():
        print(total)
        print(num)
    else:
        print("please enter a valid answer")
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
        print("goodbye".title())
        break
    num = add()
    if num == False:
        print("goodbye".title())
        break
