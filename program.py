from math import pi
Circlediameter= float(input("Please enter the diameter of the circle:"))
if Circlediameter>0:
    Circleradius= float(Circlediameter/2)
    CircleArea= pi * Circleradius**2
    print("The area of the circle:")
    print(CircleArea)
    CircleCircumference = 2* pi * Circleradius
    print("The circumference of the circle:")
    print(CircleCircumference)
elif Circlediameter<=0:
    print("Error, number must be positive")
