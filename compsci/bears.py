bears = {"Grizzly":"angry", "Brown":"friendly", "Polar":"friendly"}

for bear in bears:
    if bears[bear] == "friendly":
        print("Hello, "+bear+" bear!")
    else:
        print("odd")
