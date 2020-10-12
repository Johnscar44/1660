hungry = False
coworkers_going = False
brought_lunch = False


if hungry and coworkers_going == True:
    print("going")
elif brought_lunch and not coworkers_going == True:
    print("not going")
elif coworkers_going == True:
    print("going")
elif hungry and not brought_lunch == True:
    print("going")
elif hungry == False:
    print("not going")
