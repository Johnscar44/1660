def adding_report():
    return int(input("enter int!: "))



while True:
     choose = input("choose a report type\n\"a\" or \"t\"\nA makes a list and gets total t just outputs total\nQ or quite to leave:  ")
     if choose.lower().startswith("q"):
        print("goodbye".title())
        break
     elif choose.lower() == "t":
        print("enter int!: ")
     elif choose.lower() == "a":
         print("")
     else:
         report = adding_report()
         if report :
             print(report)
         elif report.isalpha().startswith("q").lower() == True:
             print(report + report)
         else:
             print(report)
