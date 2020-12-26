mbytes_inp = int(input("enter number of megabytes"))
print("megabytes =", mbytes_inp)
kbytes_inp = mbytes_inp * 1024
bytes_inp = kbytes_inp * 1024
print("in ", mbytes_inp, "megabytes", kbytes_inp, "kylobytes", "and", bytes_inp, "bytes")