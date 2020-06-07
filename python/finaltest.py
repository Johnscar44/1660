def add_stuff():
    return input("enter int: ")

while True:
    adding = add_stuff()
    if adding:
        print(int(adding) + int(adding))
