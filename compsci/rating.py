rating = "R"
age = 18


if rating == "G":
    print("You may see that movie!")
elif rating == "R":
    if age >= 17:
        print("You may see that movie!")
    else:
        print("You may not see that movie!")
elif rating == "PG-13":
    if age >= 13:
        print("You may see that movie!")
    else:
        print("You may not see that movie!")
elif rating == "PG":
    if age >= 8:
        print("You may see that movie!")
    else:
        print("You may not see that movie!")
else:
    if rating == "NC-17":
        print("You may not see that movie!")
