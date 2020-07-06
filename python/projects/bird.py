def bird_aval(bird = input("What bird are you looking for?: ")):
    birds = "cow , robin , parrot , eagle , sandpiper , hawk , pigeon"
    return(bird.lower().upper() in birds.lower().upper())

is_bird = bird_aval()
print("bird avalible is" , is_bird)
