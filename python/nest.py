bird = "sparo"
guess = input("Guess the bird!: ")
if guess != bird:
    second_guess = input("inccorrect two more guesses: ")
    if second_guess != bird:
        third_guess = input("inccorrect one more chance: ")
        if third_guess != bird:
            print("No more guesses GAME OVER!!")
        else:
            print("by the skin of your teeth you lucky fuck".title ())
    else:
        print("Correct second try!")
else:
    print("first try!")
