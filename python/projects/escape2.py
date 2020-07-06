my_bird = "sparo"

def get_guess():
    """Get a guess from the user """
    return input("Guess a type of bird!: ")


# try 3 times max
for i in range(2):
    guess = get_guess()
    if guess == my_bird:
        print("You gues the Motha fuckin bird")
        break
    else:
        if i == 0:
            print("Incorrect, you have two more guesses...")
        elif i == 1:
            print ("Incorrect, you have onw more guess...")
        else:
            print("Incorect!\nGame Over!")
            break
