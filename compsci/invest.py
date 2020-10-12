import math

principal = 5000
rate = 0.05
time = 5
goal = 6300

amount = principal * math.e ** (rate * time)
rounded_diff = round(amount, 2)
extra_money = rounded_diff - goal
needed_money = goal - rounded_diff

if amount >= goal:
    print("You'll exceed your goal by" , round(extra_money, 2))
else:
    print("You'll fall short of your goal by" , round(needed_money, 2))
