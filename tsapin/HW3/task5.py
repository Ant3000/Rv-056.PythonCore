# HW3_Task 5
# Calculate the length of the hypotenuse on the two entered other sides of the right triangle.

# import math module
import math

# user inputs
triangle = {
    'a': float(input("Enter the triangle's side 'A': ")),
    'b': float(input("Enter the triangle's side 'B': "))
    }

# calculation
hypotenuse = math.sqrt(triangle['a']**2 + triangle['b']**2)

# print the result
print("The length of right triangle hypotenuse 'C' = ", hypotenuse)