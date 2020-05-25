#Enter cheese order weight (numeric value): 113
#113.0 is more than currently available stock
#Enter cheese order weight (numeric value): .15
#0.15 is below minimum order amount
#Enter cheese order weight (numeric value): 2
#2.0 costs $15.98

max_weight = 101
min_weight = 10

weight = float(input("how much cheese do you want? max 100/min 10: "))
if weight > max_weight:
    print(weight , "That is over the maxiumum order amount.")
elif weight > min_weight:
    print(weight , "cost" , weight * 2.05)
else:
    print( weight , "That is below minimum order amount.")
