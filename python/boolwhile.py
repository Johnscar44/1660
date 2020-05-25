animal_name = input("Input animal name: ")
animal_count = 0

while animal_count > 4:
    if animal_name.isalpha().startswith("e") == "exit":
        break
    elif animal_name += 1:
    print(animal_name , animal_count)
    else:
    print("not valid entry")
animal_count += 1
print(animal_count , animal_name)
