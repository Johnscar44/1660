story = "A"
text = "B"
role = "C"
director = "D"
cast = "F"
for z in story:
    if z == "A":
        z = 6
    if z == "B":
        z = 5
    if z == "C":
        z = 4
    if z == "D":
        z = 2
    if z == "F":
        z = 0
for y in text:
    if y == "A":
        y = 5
    if y == "B":
        y = 4
    if y == "C":
        y = 3
    if y == "D":
        y = 1
    if y == "F":
        y = 0
for x in role:
    if x == "A":
        x = 4
    if x == "B":
        x = 3
    if x == "C":
        x = 2
    if x == "D":
        x = 1
    if x == "F":
        x = 0
for w in director:
    if w == "A":
        w = 3
    if w == "B":
        w = 2
    if w == "C":
        w = 1
    if w == "D":
        w = 0
    if w == "F":
        w = 0
for v in cast:
    if v == "A":
        v = 2
    if v == "B":
        v = 1
    if v == "C":
        v = 0
    if v == "D":
        v = 0
    if v == "F":
        v = 0
score = z + y + x + w + v
print(score)
if score == 20:
    print("perfect score")
elif score >= 17 and score <= 19:
    print("must do")
elif score >= 14 and score <= 16:
    print("seriously consider")
elif score >= 12 and score <= 13:
    print("on the bubble")
else:
    print("pass")
