#Implement a calculator that translates the amount of information entered by the user in bytes into kilobytes and megabytes

bytes_count = int(input("Enter the bytes count:  "))

kb = bytes_count / 1000       #bytes to kilobytes
mb =  bytes_count / 1e+6      #bytes to megabytes

print ("You enter:", bytes_count, "bytes."  )
print ("After converting, you have:", kb, "kilobytes." )
print ("After converting, you have:", mb, "megabytes." )