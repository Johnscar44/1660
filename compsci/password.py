entered = "abc12"
password = "abc123"
tries = 3


if tries <= 3:
    if entered == password:
        print("Login successful.")
    else:
        print("Incorrect password.")
else:
    print("Tries excceded.")
