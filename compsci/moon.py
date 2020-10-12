phase = "Full"
distance = 228000
date = 28
eclipse = True

# - Super Moon: the full moon occurs when the moon is at its closest approach to earth (less than 230,000km away).
# - Blue Moon: the second full moon in a calendar month. In other words, any full moon on the 29th, 30th, or 31st of a month.
# - Blood Moon: a lunar eclipse during a full moon.


if phase == "Full" and distance < 230000 and date >= 29 and eclipse == True:
    print("Super Blue Blood Moon")
elif phase == "Full" and date <= 28 and distance < 230000 and eclipse == True:
    print("Super Blood Moon")
elif phase == "Full" and date >= 29 and eclipse == True:
    print("Blue Blood Moon")
elif phase == "Full" and distance < 230000 and date >= 29 and eclipse == False:
    print("Super Blue Moon")
elif phase == "Full" and distance < 230000 and date <= 29 and eclipse == False:
    print("Super Moon")
elif phase == "Full" and distance > 230000 and date <= 29 and eclipse == False:
    print("Full Moon")
elif phase == "Full" and distance > 230000 and date <= 29 and eclipse == True:
    print("Blood Moon")
elif phase == "Full" and distance > 230000 and date >= 29 and eclipse == False:
    print("Blue Moon")
else:
    print("Moon")
