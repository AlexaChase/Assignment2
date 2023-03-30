from math import pi
diameter=input ("Please enter the diameter of the circle:")
radius= diameter/2
if diameter == float:
    area= radius.exp(2)*pi
    print(area)
    circumference = 2 * radius * pi
    print(circumference)
else:
    print("Error")
