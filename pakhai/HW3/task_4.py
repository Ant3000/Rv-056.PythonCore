# Calculate the area and perimeter of the circle over an entered radius.

import math

radius = int(input("Enter the radius of the circle:  "))

print("Area of the circle: ", math.pi* (radius ** 2) )
print("Perimeter of the circle: ", radius * (math.pi *2) )