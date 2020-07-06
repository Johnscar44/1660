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
#checks for digit entry loops untill one is given. do_exit referenced again. holds "total" + "items"  sends them to while loop
def add():
    x = items
    y = total
    num = input("enter int: ")
    if do_exit(num):
        return False
    if num.isdigit():
        print(num)
    elif num == "done".lower():
        return num
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

#takes gathered items and total outputs them "\n" with total of the items(numbers)
data = get_report_type()
while True:
    items = ""
    total = 0
    if data == False:
        print("goodbye".title())
        break
    num = add()
    if num == False:
        print("goodbye2")
        break
    if num == True:
        items += num + '\n'
        total += int(num)
        print(num)
    elif num == "done".lower():
        print("")
        print("items\n",items)
        print("total:" , total)
