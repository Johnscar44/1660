print("welcome to my gun game!\nyou have 30 rounds in your gun use them up!\nyou also have health for a different ending".title())
print("intructions.. \ninputs are!")
print("pulltrigger\nholdtrigger\n")
print("pulltrigger shoots once \nholdtigger shoots 10 times")
print("type [exit] or [e] to leave the game")

times_shot = 0
total_rounds = 30
total_health = 100


while True:
    click = input("shoot the gun!: ".title())
    if click.lower().startswith("e"):
        print("we shot you in the back!\nyour dead now.. lol".title())
        break
    elif click == "pulltrigger".lower():
        times_shot += 1
        print("bang!".upper())
    elif click == "holdtrigger".lower():
        times_shot += 10
        print("bang\n" * 10)
    else:
        print('that is not a command! We shot you!')
        total_health -= 20
    times_shot += 1
    if total_rounds < times_shot:
        print("congrats!! you are now wanted for the murder of mulitiple people!".title())
        print("thanks for playing scumbag!".title())
        break
    elif total_health <= 0:
        print("your dead... \n im not sure how this was a very easy game...")
        print("well either way my god have mercy on your soul you fuckin idiot..".title())
        break
