from math import sqrt
print("введіть катети трикутника:")
a = float(input("a: "))
b = float(input("b: "))
c = sqrt(a**2 + b**2)
print("довжина гіпотенузи є", c )