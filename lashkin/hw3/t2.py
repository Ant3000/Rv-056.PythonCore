#take input
bytes = input ('How many bytes do you want to convert? ')

#check if input is propper
if bytes.isnumeric() == False:
    print('You provided NOT a number/negative number! Try again using positive numbers.')
    exit()

bytes = float(bytes)

#calculating
kilobytes = bytes / 1024
megabytes = bytes / 1048576

#providing result
print(f'{bytes} bytes = {kilobytes} kB')
print(f'{bytes} bytes = {megabytes} MB')