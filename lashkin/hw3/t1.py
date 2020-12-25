from time import sleep


var1 = input ('Provide 1st variable! ')
var2 = input ('Provide 2nd variable! ')

print(f'Your 1st variable is {var1}, your 2nd variable is {var2}')
print('And now swap is coming...')

sleep(2.5)

var1, var2 = var2, var1

print(f'So, your 1st variable now is {var1}, your 2nd variable is {var2}')