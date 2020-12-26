# HW3_Task 2
# Implement a calculator that translates the amount of information entered by the user 
# in bytes into kilobytes and megabytes

# user input
byte = float(input("Please enter the value in bytes: "))

# convertion
kilobyte = byte * 2**(-10)
megabyte = byte * 2**(-20)

# print the result
print("Result: {} byte = {} kilobyte = {} megabyte".format(byte, kilobyte, megabyte))