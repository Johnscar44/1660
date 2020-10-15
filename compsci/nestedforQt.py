beats_per_measure = 4
measures = 5
for j in range(1,measures+1):
    for x in range(1,beats_per_measure + 1):
        print(x)
print("")
print("")
print("")
print("")
print("")
for i in range(1, 6):
    j = 0
    while j < i:
        print(j, end = " ")
        j += 1
    print("")

for i in range(1, 6):
    for j in range(0, i):
        print(j, end = " ")
    print("")
i = 0
while i < 6:
    j = 0
    while j < i:
        print(j, end = " ")
        j += 1
    i += 1
    print("") 
