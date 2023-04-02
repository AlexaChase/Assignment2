from math import pi
Circlediameter= float(input("Please enter the diameter of the circle:"))
Circleradius= float(Circlediameter/2)
CircleArea= pi * Circleradius**2
CircleCircumference = 2* pi * Circleradius
if Circlediameter>0:
    print("The area of the circle:")
    print(CircleArea)
    print("The circumference of the circle:")
    print(CircleCircumference)
elif Circlediameter<=0:
    print("Error, number must be positive")
elif CircleCircumference<=0:
    print("Error, output was negative")
elif CircleArea<=0:
    print("Error, output was negative")
