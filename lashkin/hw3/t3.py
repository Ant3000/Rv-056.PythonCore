#take input
hight = input ('Hight: ')
width = input ('Width: ')

#check if input is propper
if hight.isnumeric() == False or width.isnumeric() == False:
    print('You provided NOT a number/negative number! Try again using positive numbers.')
    exit()

hight = float(hight)
width = float(width)

if hight == 0 or width == 0:
    print('You can\'t provide 0 lenghts! Try again using positive number.')
    exit()

#calculate
area = width * hight
perimetr = 2 * (width + hight)

print(f'Area is {area}, perimetr is {perimetr}.')

if width == hight:
    print('Nice fact: your rectangle is square :)')