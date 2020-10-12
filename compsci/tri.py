#Get the first side from the user
side1 = int(input("Enter the shortest side: "))
#Get the second side from the user
side2 = int(input("Enter the next shortest side: "))
#Get the third side from the user
side3 = int(input("Enter the longest side: " ))

#Check if the shorter sides' sum exceeds the longer side
result = (side1 + side2) >= side3
#Print the result
print("'These sides can form a triangle' is", result)
