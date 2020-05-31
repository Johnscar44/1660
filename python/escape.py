#\n return new line
#\t tab makes a tab in line
#\' Single quote
#\" Double quote
#\\ Backslash



#print("this is awesome \n I have to figure this out \t \'or i will end up working at shore point\' \n for the rest of \"of my damn life\" \t if that happends ill \\\killmyself//".title())


#print("\\\WARNING///")

#`````

#Function has a single string parameter that it checks s is a single word starting with "pre"

#Check if word starts with "pre"
#Check if word .isalpha()
#if all checks pass: return True
#if any checks fail: return False
#Test
#get input using the directions: *enter a word that starts with "pre": *
#call pre_word() with the input string
#test if return value is False and print message explaining not a "pre" word
#else print message explaining is a valid "pre" word
# [ ] create and test pre_word()





def pre_word(word = input("word that starts with pre: ")):
    if word.startswith("pre") == True:
        print("word starts with pre")
    else:
        if word.isalpha() == True:
            print("word does not start with pre")
        else:
            print("is not a word")
