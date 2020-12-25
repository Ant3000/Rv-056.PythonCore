#take input
_bytes = input ('How many bytes do you want to convert? ')

#check if input is propper
if _bytes.isnumeric() == False:
    print('You provided NOT a number/negative number! Try again using positive numbers.')
    exit()

_bytes = float(_bytes)

#calculating
kilobytes = _bytes / 1000
megabytes = _bytes / 1000000

#providing result
print(f'{_bytes} bytes = {kilobytes} kB')
print(f'{_bytes} bytes = {megabytes} MB')