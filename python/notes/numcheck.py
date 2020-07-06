





while True:
    number = input("enter a word or integer: ")
    if number == "":
        print("can not be empty")
    elif int(number) > 99:
        print("big number")
    elif int(number) < 20:
        print("small number")
    elif number.isalpha() == True:
        print("all letters")
    else:
        print("multiple charactor types")
        break
