mystery_string = "CS1301"

#Write a for-each loop that lists each character in
#mystery_string with its index. For example, if the string
#was "David", the output would be:
#0 D
#1 a
#2 v
#3 i
#4 d
#
#Note that the first item is #0, the second is #1, and so
#on! We'll talk about why that is in Unit 4.
#
#Hint: You'll need a separate variable to keep track of how
#many letters you've printed! You may not use the range
#function on this problem.


#Add your code here!
count = -1
for i in mystery_string:
    count += 1
    print(count , i)
print("")
print("")
print("")
print("")
print("")
#Creates listOfNumbers and assigns it to a list of ten
#numbers, 91 through 100
listOfNumbers = [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
sum = 0

#Runs this loop once for each item, assigning the current
#item to the variable 'currentNumber'
for currentNumber in listOfNumbers:
    sum += currentNumber
#Divides sum by the number of items in the list
print(sum / len(listOfNumbers))
