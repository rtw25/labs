import math

radius = int(input("enter the radius: "))

perimeter = (2*radius*math.pi)

roundedPerimeter = f"{perimeter:.2f}"


area = math.pi * radius**2
roundedArea = f"{area:.2f}"

print("The circle with radius",radius, "has an area of", roundedArea, "and a perimeter of", roundedPerimeter )
