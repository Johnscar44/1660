print("****************************")
print("**         THIS           **")
print("**         GAME           **")
print("**          IS            **")
print("**         DUMB           **")
print("****************************")


#gets the username from the user and returns it to the while loop
def get_username(name):
    while True:
        name = input("input username: ")
        if name == 'e'.upper():
            print("goodbye".title())
            break
#doesnt let the user make a user name longer then 16 charactors
        elif len(name) >= 16:
            print("username too long")
        else:
            are_you_sure()



#makes sure user is happy with username
def are_you_sure():
    sure = input("are you sure? \n [y] [n]: ")
    if sure == 'n':
        get_username()#runs get_username again if users says n for no
    elif sure == 'y':#returns the user name to while loop in sure variable
        print(sure)
    else:
        print("Not Valid Input [y] or [n]")#only input here avalible is y or n
                                           #returns to top of are_you_sure
get_username("john")
