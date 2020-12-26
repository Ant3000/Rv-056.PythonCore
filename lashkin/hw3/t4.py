from math import pi


#take input
radius = input ('Radius: ')

#check if input is propper
if radius.isnumeric() == False:
    print('You provided NOT a number/negative number! Try again using positive numbers.')
    exit()

radius = float(radius)

if radius == 0:
    print('You can\'t provide 0 lenghts! Try again using positive number.')
    exit()

#calculate
area = pi * radius**2
perimetr = 2 * pi * radius

area = round(area, 3)
perimetr = round(perimetr, 3)

print(f'Area is {area}, perimetr is {perimetr}.')