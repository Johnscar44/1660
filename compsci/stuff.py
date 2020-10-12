print("****************************")
print("**         THIS           **")
print("**         GAME           **")
print("**          IS            **")
print("**         DUMB           **")
print("****************************")
print("### input [quit] to exit ###".title())

#gets the username from the user and returns it to the while loop
def get_username(name):
    while True:
        name = input("input username: ")
#        quit = exit_now("quit")
#        if quit == True:
#            return False
        if name == 'quit':  #returns false to while loop for quitting in get_unsername function
            return False
#doesnt let the user make a user name longer then 16 charactors
        elif len(name) >= 16:
            print("username too long")
#user name cant be shorter then 3 charactors
        elif len(name) <= 3:
            print("username too short")
        else:
            return name



#makes sure user is happy with username
def are_you_sure():
    while True:
        sure = input("are you ready? \n [y] [n]: ")
        if sure == 'n':
            return False
        elif sure == 'y': #returns yes or no to while loop
            return True
        else:
            print("Not Valid Input \n please choose [y] or [n]")#only input here avalible is y or n

def exit_now(word):
    if word == "quit":
        return True

score = 0
user = get_username("name")
while True:
    if user == "quit":
        print("goodbye!".title())
        break
    elif user:
        im_sure = are_you_sure()
        if im_sure == False:
            print("resetting username".title())
            user = get_username("name")#renames user varible if the user is unhappy with original selection
        elif im_sure == True:                   #makes is so selecting username can loop untill confermed
            print("username selected".title()) #conferms username selection and shows rules and controls
            print("OK" , user , "Welcome to [Game Title here!] Listen carefully to the rules")
            print("How to play")
            print("rules")
            ready = are_you_sure() #runs are_you_sure again to make sure user is ready to start the game
            if ready == False:
                print("Goodbye2")
                break
            elif ready == True:
                print("OK! Lets Go!")
                break
