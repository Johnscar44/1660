chances = 0
while True:
    user_name = input("user name: ".title())
    if user_name == "John Scarpino":
        print("correct")
        password = input("password: ".title())
    elif password == "589Vaughn":
            print ("Acount Number-")
            print("Rounting Number-")
    elif chances == 3:
        break
    else:
        chances += 1
        print("incorrct")
