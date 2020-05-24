#Enter cheese order weight (numeric value): 113
#113.0 is more than currently available stock
#Enter cheese order weight (numeric value): .15
#0.15 is below minimum order amount
#Enter cheese order weight (numeric value): 2
#2.0 costs $15.98

max_weight = "100"
min_weight = "10"

weight = input("how much cheese do you want? max 100/min 10: ")
if weight.isdigit() == False:
    print("Entry must be a digit")
elif weight > max_weight:
    print("That is over the max weight")
elif weight < min_weight:
    print("That is not enough")
else:
    print(weight , "cost" , float(weight) * 2.05 )
