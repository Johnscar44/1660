lyrics = ["I wanna be your endgame", "I wanna be your first string",
          "I wanna be your A-Team", "I wanna be your endgame, endgame"]
lines_of_sanity = 8




#Write some code that will print the lyrics that run through
#your head. It should keep repeating each line one-by-one
#until you've reached lines_of_sanity lines. Then, it should
#keep going to finish out the current verse. After that, print
#"MAKE IT STOP" in all caps (without the quotes).
#
#HINT: Remember, we can iterate through items in a list using
#this syntax:
#
#  for item in list_of_items:
#
#HINT 2: You'll probably need a counter to count how many lines
#have been printed so far.
#Add your code here! Using the initial inputs from above, this
#should print 9 lines: all 4 lines of the list twice, followed
#by MAKE IT STOP

while lines_of_sanity > 0:
    for x in lyrics:
        lines_of_sanity -= 1
        print(x)
print("MAKE IT STOP")
