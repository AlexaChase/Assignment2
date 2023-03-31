from math import pi
d= input ("Please enter the diameter of the circle:")
if d == float or int:
    r= input(d)/2 #division
    a= r.exp(2)*pi
    print(a)
    c = 2 * r * pi
    print(c)
else:
    print("Error")
