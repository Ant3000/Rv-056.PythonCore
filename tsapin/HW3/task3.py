# HW3_Task 3
# Calculate the area and perimeter of the rectangle for an entered width and height.

# user inputs
rectangle = {
    'length': float(input("Enter the rectangle length: ")),
    'width': float(input("Enter the rectangle width: "))
    }

# calculations
area = rectangle['length'] * rectangle['width']
perimeter = 2 * (rectangle['length']+rectangle['width'])

# print the result
print("Area of rectangle = ", area)
print("Perimeter of rectangle = ", perimeter)