cut = "Oval"
clarity = "F"
color = "Z"
carat = 2.7
budget = 4750
preferred_cuts = ["Round", "Radiant", "Oval", "Heart", "Pear", "Cushion"]


base_cost = 100
diff = ord(color) - ord("D")
dep = diff*0.2
color_cost = base_cost - dep
cost = 0

if clarity == "SI":
    cost = color_cost*2
elif clarity == "VS":
    cost = color_cost*4
elif clarity == "VVS":
    color_cost*8
elif clarity == "IF":
    cost = color_cost*16
elif clarity == "F":
    cost = color_cost*32

price = cost*carat

if price <= budget and cut in preferred_cuts:
    print("I'll take it!")
else:
    print("No thanks")
