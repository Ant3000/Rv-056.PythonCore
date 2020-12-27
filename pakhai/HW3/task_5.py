# Calculate the length of the hypotenuse on the two entered other sides of the right triangle.

import math

side_A = int(input("Enter the first side of triangle:  "))
side_B = int(input("Enter the second side of triangle:  "))

print("Length of the hypotenuse: ", math.sqrt(side_A*side_A + side_B*side_B) )