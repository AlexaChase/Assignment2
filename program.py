from math import pi
Circlediameter= float(input("Please enter the diameter of the circle:"))
if Circlediameter>0:
    Circleradius= float(Circlediameter/2)
    CircleArea= pi * Circleradius**2
    print(CircleArea)
elif Circlediameter<=0:
    print("Error, number must be positive")
