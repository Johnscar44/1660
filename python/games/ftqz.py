#tf_quiz() has 2 parameters which are both string arguments
#question: a string containg a T/F question like "Should save your notebook after edit?(T/F): "
#correct_ans: a string indicating the correct answer, either "T" or "F"
#tf_quiz() returns a string: "correct" or "incorrect"
#Test tf_quiz(): create a T/F question (or several!) to call tf_quiz()
# [ ] Create the program, run tests

greeting = "true or false quiz"
print(greeting.title())

def tf_quiz(question , answer):
    print(question)
    tf = input("T/F?: ")
    if answer == tf.lower().upper():
        print("correct")
    else:
        print("incorrect")

quiz_eval = tf_quiz("balls are round" , "F")

print("Your Answer Is?" , quiz_eval)
