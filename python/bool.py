#using single and double quotes in a string
cm_height = "172"
print("cm_height:",cm_height,"is all digits =",cm_height.isdigit())

#way one of printing bool only works with strings
string = "python"
print(string.isalpha())

#way two with out makeing a "python" veriable
print("python".isalpha())


#boolean string test methods  true or false
#.isalpha()
#.isalnum()
#.istitle()
#.isdigit()
#.islower()
#.isupper()
#.startswith()


print("hello".isupper())

print("HELLO".isupper())

print("1234".isdigit())

print("HELLO".startswith("i"))

length = "33"
print(length.isalnum())
