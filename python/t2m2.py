def tf_quiz(question , answer):
    answer = input("T/F: ")
    if answer == T.lower():
        print("correct")
    else:
        print("inccorrect")

quiz_eval = tf_quiz("balls are round" , "T")
print("your anwser is" ,quiz_eval)
