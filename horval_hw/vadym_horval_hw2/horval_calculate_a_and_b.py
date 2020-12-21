# Homework on lesson 1 Vadym Horval
a = input("Please enter the Integer numeric value a=")

while True: # check value for digital
     try:
         a = int(a)
         break
     except ValueError:
         a = input("That was no valid number. Try again enter the Integer numeric value a=")

b = input("Please enter the Integer numeric value b=")

while True: # check value for digital
     try:
         b = int(b)
         break
     except ValueError:
         b = input("That was no valid number. Try again enter the Integer numeric value b=")

print("a + b =",(a+b))
print("a - b =",(a-b))
print("a * b =",(a*b))

if a !=0: # check dision by 0
    print("a / b =",(a/b))
else:
    print("Operation a / b is not possible")
