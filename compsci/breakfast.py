egg = False
milk = False
butter = False
flour = False

# 1. pancakes: egg, milk, butter, flour
# 2. omelette: egg, milk, butter
# 3. custard: egg, milk
# 4. poached eggs: egg

if egg == True and milk == True and butter == True and flour == True:
    print("pancakes")
elif egg == True and milk == True and butter == True:
    print("omelette")
elif egg == True and milk == True:
    print("custard")
elif egg == True:
    print("poached eggs")
else:
    print("Go to the store")
