print("****************************")
print("**         THIS           **")
print("**         GAME           **")
print("**          IS            **")
print("**         DUMB           **")
print("****************************")


#gets the username from the user and returns it to the while loop
def get_username(name):
    name = input("input username: ")
    exit_now()
    #doesnt let the user make a user name longer then 16 charactors
    if len(name) >= 16:
        print("username too long")
    else:
        print(name)
        return name
#lets user leave game at anytime
def exit_now():
    exit = exit_now()
    if exit.startwith("e".upper()):
        return False

get_username("john")
