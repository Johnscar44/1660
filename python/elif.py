secret_num = "2"

guess = input("guess the number 1 - 3: ")
if guess.isdigit() == False:
    print("answer can only be a digit")
elif guess == "1":
    print("Too Low")
elif guess == "2":
    print("You guessed it!")
elif guess == "3":
    print("Too high")
else:
    print("Guess not in rage 1 - 3")
    print("please try again")
