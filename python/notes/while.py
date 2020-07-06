while True:
    familar_name = input("type common name: ")
    if familar_name.isalpha() == True:
        print(familar_name , "is great thank you")
        break
    else:
        print("that is not a single name \n or \n no specail characters")




number_guess = "0"
sec_number = "5"

while True:
    number_guess = input("guess a number between 1 and 5: ")
    if number_guess == sec_number:
        print("yes that is the correct number")
        break
    else:
        print(number_guess , " incorrect try again!")
