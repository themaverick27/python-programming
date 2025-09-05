# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math

def cirlce_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius

    return area, circumference


area, circum = cirlce_stats(3)
print("Area:",area)
print("Circumference:",circum)

# rounded decimal places upto 2 digits using built-in method round() - returns a float
print("Area:",round(area, 2))
print("Circumference:",round(circum, 2))

# rounded decimal places upto 2 digits using built-in method format() - returns a string
print("Area:","{:.2f}".format(area))
print("Circumference","{:.2f}".format(circum))