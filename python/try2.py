while True:
    number = input("enter a word or integer: ")
    if number == "":
        print("can not be empty")
    elif number.isalpha() == True:
        print("all letters")
    elif int(number) > 99:
        print("big number")
    elif int(number) < 20:
        print("small number")
    else:
        print("multiple charactor types")
        break
