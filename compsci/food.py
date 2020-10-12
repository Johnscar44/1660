myFood = "chocolate cupcakes"
yourFood = "hawaiian pizza"

if myFood == yourFood:
    print("We like the same food.")
else:
    print("We have different tastes.")

if len(myFood) > 8:
    print("My food has a long name.")
elif len(yourFood) > 8:
    print("Your food has a long name.")
else:
    print("We like foods with short names.")

if len(myFood) > len(yourFood):
    print("My food has a longer name than yours.")
else:
    print("Your food has a longer name than mine.")

if yourFood == "pasta":
    print("Mamma mia!")
else:
    print(yourFood)
