def get_username():
    chances = 0
    while True:
        user_name = input("user name: ".title())
        if user_name.lower() == "e":
            print("goodbye".title())
            return False
        elif user_name == "John Scarpino":
            print("correct")
            return True
        elif user_name != "John Scarpino":
            chances += 1
            print("incorrect")
            if chances == 3:
                print("out of chances")
                return False

def get_password():
    chances = 0
    while True:
        password = input("password: ".title())
        if password.lower() == "e":
            print("goodbye".title())
            return False
        elif password == "589Vaughn":
            print("correct")
            return True
        elif password != "589Vaughn":
            chances += 1
            print("incorrect")
            if chances == 3:
                print("out of chances")
                return False


name = get_username()
while True:
    if name == True:
        password = get_password()
        if password == True:
            print("stuff here")
            break
        elif password == False:
            print("wrong password")
            break
    elif name == False:
        print("wrong user name".title())
        break
