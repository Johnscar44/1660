
if x < 0:
    print("-")
else:
    if y >= 0:
        print("+/+")
    else:
        print("+/-")




if True:
    if False:
        print("Banana")
    else:
        print("Apple")
else:
    if True:
        print("Dates")
    else:
        print("Corn")




sandwich_type = input('"c" for Cheese or "v" for Veggie Special: ')

if sandwich_type.lower() == "c":
    # select cheese type
    cheese_type = input('"c" for Cheddar or "m" for Manchego: ')

    if cheese_type.lower() == "c":
        print("Here is your Cheddar Cheese sandwich")
    else:
        print("Here is your Manchego Cheese sandwich")

else:
    print("Here is your Veggie Special")









# full example: handling some invalid input and elif statement
# [ ] review the code then run following the flowchart paths including **invalid responses** like "xyz123"

# ***TIP:*** click in input box before typing
print("Hi, welcome to the sandwich shop.  Please select a sandwich.")
sandwich_type = input('"c" for Cheese or "v" for Veggie Special: ')
# select sandwich type sandwich_type = input('"c" for Cheese or "v" for Veggie Special: ')
print()

if sandwich_type.lower() == "c":
    # select cheese type
    print("Please select a cheese.")
    cheese_type = input('"c" for Cheddar or "m" for Manchego: ')
    print()

    if cheese_type.lower() == "c":
        print("Here is your Cheddar Cheese sandwich.  Thank you.")
    elif cheese_type.lower() == "m":
        print("Here is your Manchego Cheese sandwich.  Thank you.")
    else:
        print("Sorry, we don't have", cheese_type, "choice today.")

elif sandwich_type.lower() == "v":
    print("Here is your Veggie Special. Thank you.")

else:
    print("Sorry, we don't have", sandwich_type, "choice today.")
print()
print("Goodbye!")
