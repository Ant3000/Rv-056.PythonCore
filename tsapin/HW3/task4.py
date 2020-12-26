# HW3_Task 4
# Calculate the area and perimeter of the circle over an entered radius.

# import math module
import math

# user input
radius = float(input("Enter the circle radius: "))

# calculations
area = math.pi * radius**(2)
perimeter = 2 * math.pi * radius

# print the result
print("Circle area = ", area)
print("Circle perimeter = ", perimeter)