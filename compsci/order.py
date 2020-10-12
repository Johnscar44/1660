item = "burrito"
meat = "steak"
queso = True
guacamole = False
double_meat = False
# - The base price for a quesadilla is 4.00, for nachos is
#   4.50, and for burritoes is 5.00.
# - If meat is steak or pork, add 0.50. Any other meat adds
#   no money to the price.
# - guacamole always adds 1.00 to the price.
# - queso adds 1.00 to the price UNLESS the item is nachos,
#   in which case it adds nothing.
# - double_meat adds 1.50 if the meat is steak or pork, or
#   1.00 otherwise.
if item == "nachos":
    base_price = 4.5
elif item == "quesadilla":
    base_price = 4.0
elif item == "burrito":
    base_price = 5.0

if meat == "steak":
    base_price += 0.50
if meat == "pork":
    base_price += 0.50
elif meat == "steak" and double_meat:
    base_price += 1.50
elif meat == "pork" and double_meat:
    base_price += 1.50
elif double_meat:
    base_price += 1.0

if guacamole:
    base_price += 1.0
if queso and item != "nachos":

    base_price += 1.0

print(base_price)
