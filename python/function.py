greet = "hello and welcome, to your class schedule!"
print(greet.title())
period = "three"
classes = "math history and english"
print()
print("You have" , period , "classes of" , classes , "!")
print()
def make_schedule(period1, period2 , period3):
    schedule = ("[1st]" + period1.title() + " [2nd]" + period2.title() + " [3rd]" + period3.title())
    return schedule

student_schedule =  make_schedule("mathematics" , "history" , "english")
print("SCHEDULE:", student_schedule)
print()
print("You will be expected to show up five minutes before class.")

def low_case(words_in):
    return words_in.lower()

words_lower = low_case("Return THis lower")
print(words_lower)
