import math
sideA = int(input("choose a number for side 1: "))
sideB = int(input("choose a number for side 2: "))


hypotenuse = math.sqrt(((sideA)**2) + ((sideB)**2))

roundedHypotenuse = f"{hypotenuse:.2f}"

print (roundedHypotenuse)
