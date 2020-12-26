# HW3_Task 1
# User enters two numbers: a and b. Swap the values of variables a and b
# without using the additional variable.

# enter a and b
dict = {
    'a': int(input("Please enter a = ")),
    'b': int(input("Please enter b = "))
    }

# before swap
print("Before swap: ", dict)

# swap
dict.update({
    'a': dict['b'],
    'b': dict['a'],
     })

# after swap
print("After swap: ", dict)