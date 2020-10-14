a_string = "Indices! Yay!"
a_character = a_string[3]
print("The character is", a_character)


some_range = range(5, 10)
print(some_range[0])
print(some_range[4])


some_string = "Georgia Tech"
print(some_string[0])
print(some_string[8])

some_list = ["I", "like", "shorts", "they're", "comfy", "and", "easy", "to", "wear"]
print(some_list[0])
print(some_list[4])

for i in range(5, 9):
    print("Index", i)

some_string = "Georgia Tech"
for i in range(0, len(some_string)):
    print(i, some_string[i])
print("")
print("")
print("")
some_list = ["I", "like", "shorts", "they're", "comfy", "and", "easy", "to", "wear"]
for i in range(0, len(some_list)):
    print(i, some_list[i])
