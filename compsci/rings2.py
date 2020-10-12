cut = "emerald"
clarity = "VS"
color = "E"
carat = 1.1
budget = 500
preferred_cuts = ["emerald", "cushion", "princess", "oval"]


if cut in preferred_cuts:
    cost = 100
    percent_off = (ord(color) - ord("D")) * 0.02
    cost *= 1 - percent_off
if not clarity == "I":
        cost *= 2
        if not clarity == "SI":
            cost *= 2
            if not clarity == "VS":
                cost *= 2
                if not clarity == "VVS":
                    cost *= 2
                    if not clarity == "IF":
                        cost *= 2
cost *= carat

if cost <= budget:
    print("I'll take it!")
else:
    print("No thanks")
    print("No thanks")
