#[ ] add code below testing the menu string variable for 'pizza', 'soup', and 'dessert' using keyword   in

#print each test on a separate line
#print a description for each test   (e.g. - "Pizza in menu = True")
# [] print 3 tests, with description text, testing the menu variable for 'pizza', 'soup' and 'dessert'
#menu = "salad, pasta, sandwich, pizza, drinks, dessert"
#Program: What is on the menu
#[ ] Create a program where a user can check if an item is on the menu
#store the user response in a variable menu_ask
#use the menu from above and add some additional items
#the program should be able to ignore case mismatch so that "hello" is found in "Hello World!"
# Create a program where the user supplies input to search the menu
#[ ] Challenge: Add to the menu
#print the current menu
#get user input for add_item variable
#new_menu use string addition to add add_item to menu
#print the new_menu
#testing

#check if an item is on the menu, check for previous items and the item you added
# add to menu
# Testing Add to Menu - create user input to search for an item on the new menu

menu = ", salad, pasta, sandwich, pizza, drinks, dessert "
print(menu)
check_item = input("what would you like?: ")
print(check_item.lower() in menu.lower())
add_item = input("what would you like to add?: ").capitalize()
print(add_item + menu)
print(menu , " menu item added!".upper())
