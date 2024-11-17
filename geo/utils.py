import math

def pythagoras(a, b):
    """Calculate the length of the hypotenuse given sides a and b."""
    c = math.sqrt(a**2 + b**2)
    return c

def circle(r):
    """Calculate the area of a circle given radius r."""
    area = math.pi * r**2
    return area