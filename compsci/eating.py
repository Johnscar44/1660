hour = 1
minute = 0


# - Barrelhouse: Closes at 11:00PM
# - Taco Bell: Closes at 2:00AM
# - Cookout: Closes at 3:00AM
# - Waffle House: Never closes. Ever.


#Assume that this list is also a priority list: if Barrelhouse is open, you choose Barrelhouse. If not, you choose Taco Bell
#if it's open. If not, you choose Cookout if it's open. If not, you choose Waffle House.

#However, there are two wrinkles:

# - We're using 12-hour time.
# - hour will always represent a time from 10PM to 5AM.

#That means that if hour is 10 or 11, it's PM; if hour is
#12, 1, 2, 3, 4, or 5, it's AM. This will make your reasoning
#a little more complex. You may assume that all four
#restaurants open later than 6AM, though, so you don't have
#to worry about opening time, just closing time.
hour = 1
minute = 0

if hour == 10 or 11:
    print(hour)
else:
    print("go fuck yourself")
