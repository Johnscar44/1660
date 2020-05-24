#Enter cheese order weight (numeric value): 113
#113.0 is more than currently available stock
#Enter cheese order weight (numeric value): .15
#0.15 is below minimum order amount
#Enter cheese order weight (numeric value): 2
#2.0 costs $15.98

max_weight = "101"
min_weight = "9"

weight = input("how much cheese do you want? max 100/min 10: ")
if weight.isdigit() == False:
    print("Entry must be a digit")
elif weight >= max_weight:
    print(weight , "That is over the maxiumum order amount.")
elif weight <= min_weight:
    print( wieght , "That is below minimum order amount.")
else:
    print(weight , "cost" , float(weight) * 2.05 )
