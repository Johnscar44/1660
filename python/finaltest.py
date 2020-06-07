#get input from user.  check for alpha characters. make input exept lower and upper case letters. loops untill correct answer
#uses helper function do_exit for leaving functionality.  chooses a report type for listing all inputs or just total of all.
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
#checks for digit entry loops untill one is given. do_exit referenced again. prints total + num
def add():
    total = 0
    num = input("enter int: ")
    if do_exit(num):
        return False
    if num.isdigit():
        total += int(num)
        print(total)
        print(num)
    else:
        print("please enter a valid answer")
        return None

#helper funtion for exit through whole program
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
        print("peace")
        break
