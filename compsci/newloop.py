mystery_int_1 = 3
mystery_int_2 = 4
mystery_int_3 = 5

#Above are three values. Run a while loop until all three
#values are less than or equal to 0. Every time you change
#the value of the three variables, print out their new values
#all on the same line, separated by single spaces. For
#example, if their values were 3, 4, and 5 respectively, your
#code would print:


#2 3 4
#1 2 3
#0 1 2
#-1 0 1
#-2 -1 0



while mystery_int_1 > 0 and mystery_int_2 > 0 and mystery_int_3 > 0:
    mystery_int_1 -= 1
    print(mystery_int_1 , mystery_int_2 , mystery_int_3)
