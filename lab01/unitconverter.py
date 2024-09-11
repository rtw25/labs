import math
in_to_cm = 2.54
yd_to_m = 0.9144
oz_to_g = 28.349523125
lb_to_kg = 0.45359237
num = input("choose a distance or weight: ")
value, unit = num.split()

value = float(value)


if unit == "in":
    convertedValue = value * in_to_cm
    convertedUnit = "cm"
elif unit == "cm":
    convertedValue = value / in_to_cm
    convertedUnit = "in"
elif unit == "yd":
    convertedValue = value * yd_to_m
    convertedUnit = "m"
elif unit == "m":
    convertedValue = value / yd_to_m
    convertedUnit = "yd"
elif unit == "oz":
    convertedValue = value * oz_to_g
    convertedUnit = "g"
elif unit == "g":
    convertedValue = value / oz_to_g
    convertedUnit = "oz"
elif unit == "lb":
    convertedValue = value * lb_to_kg
    convertedUnit = "kg"
elif unit == "kg":
    convertedValue = value / lb_to_kg
    convertedUnit = "lb"
else:
    print ("invalid unit try again")

roundedConvertedValue = f"{convertedValue:.2f}"

print(value, unit, "=", roundedConvertedValue, convertedUnit)
