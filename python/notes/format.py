#.upper() .lower() .capitalize()
print("I'm Mr. Scarpino and I'm a Killer Badass".lower())

print("I'm Mr. Scarpino and I'm a Killer Badass".capitalize())

print("I'm Mr. Scarpino and I'm a Killer Badass".upper())

#.title() .swapcase()

print("I'm Mr. Scarpino and I'm a Killer Badass".title())

print("I'm Mr. Scarpino and I'm a Killer Badass".swapcase())



#formant input
fav_color = input("what is your favorate color?: ").upper()
print(fav_color)

fav_color = input("what is your favorate color?: ")
print(fav_color.upper())


#bool in keyword  finding a word in a string
menu = "crap shit waste smoke pizza worms"
print("Pizza" in menu)

menu = "crap, shit, waste, smoke, pizza, worms"
print("Pizza".lower() in menu.lower())


paint_colors = "red, blue, green, black, orange, pink"
print("Red".lower() in paint_colors.lower())
