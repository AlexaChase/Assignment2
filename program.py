from math import pi
Circlediameter= float(input("Please enter the diameter of the circle:"))
if Circlediameter>0:
    Circleradius= float(Circlediameter/2)
    print(Circleradius)
elif Circlediameter<0:
    print("Error, number must be positive")
