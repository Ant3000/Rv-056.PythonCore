# HW3_Task 2
# Implement a calculator that translates the amount of information entered by the user 
# in bytes into kilobytes and megabytes

# user input
byte = float(input("Please enter the value in bytes: "))

# convertion
kilobyte_decimal = byte * 10 ** (-3)
megabyte_decimal = byte * 10 ** (-6)
kilobyte_binary = byte * 2 ** (-10)
megabyte_binary = byte * 2 ** (-20)

# print the result
print("In Decimal: {} byte = {} kilobyte = {} megabyte".format(byte, kilobyte_decimal, megabyte_decimal))
print("In Binary: {} byte = {} kilobyte = {} megabyte".format(byte, kilobyte_binary, megabyte_binary))