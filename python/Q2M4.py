def str_analysis():
    return input("enter word or int: ")


while True:
    word = str_analysis()
    if word == "":
        print("field can not be empty")
    elif word.isalpha():
        print("all alphabetic")
        break
    else:
        if word.isdigit() == False:
            print("multiple characters")
        elif int(word) > 99:
            print("big number")
        elif int(word) < 99:
            print("small number")
        else:
            print("not acceptible input")
