def adding_report(r_type):
    input_string = ""
    input_total = 0
    while True:
        input_items = input("Enter an integer or \"Q\" to quit: ")
        if input_items.isdigit():
            if r_type == "A":
                input_total += int(input_items)
                input_string = input_string + "\n" + input_items
            else:
                input_total += int(input_items)
        elif input_items.upper().startswith("Q"):
            if r_type == "A":
                print("\nItems" + input_string + "\n" "\nTotal\n" + str(input_total))
                break
            else:
                print("\nTotal\n" + str(input_total))
                break
        else:
            print("Invalid input")

report_type = input("Choose Report Type(\"A\" or \"T\"): ").upper()

while True:
    if report_type == "A":
        break
    elif report_type == "T":
        break
    else:
        print("invalid input")
        report_type = input("Choose Report Type(\"A\" or \"T\"): ").upper()

adding_report(report_type)
