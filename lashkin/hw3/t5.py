import math


#take input
sideA = input ('Side A: ')
sideB = input ('Side B: ')

#check if input is propper
if sideA.isnumeric() == False or sideB.isnumeric() == False:
    print('You provided NOT a number/negative number! Try again using positive numbers.')
    exit()

sideA = float(sideA)
sideB = float(sideB)

if sideA == 0 or sideB == 0:
    print('You can\'t provide 0 lenghts! Try again using positive number.')
    exit()

#calculate

hypotenusSqrt = sideA ** 2 + sideB ** 2
hypotenus = math.sqrt(hypotenusSqrt)
hypotenus = round(hypotenus, 2)

print(f'Hypotenus is {hypotenus}.')

if sideB == sideA:
    print('Nice fact: your triangle is isosceles :)')