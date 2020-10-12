mystery_string = "zizazzle"

# - If z appears three or more times in a row, print "I'm sleepy..."
# - If z appears two times in a row, print "I love ZZ Top!"
# - If z appears once, print "One is the loneliest number."
# - If z does not appear, print "Who needs z anyway?"

if "zzz" in mystery_string:
    print("I'm  sleepy...")
elif "zz" in mystery_string:
    print("I Love ZZ Top!")
elif "z" in mystery_string:
    print("ONe is the loneliest number.")
else:
    print("Who needs z anyway?")
