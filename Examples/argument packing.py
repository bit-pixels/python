# *args. Parameter which will pack all arguments into a tuple. useful so that a function cna accept a varying amount of
# arguments For example:

def add(*args):
    a = 0
    for i in args:
        a += i
    return a


print(add(72, 823, 92))    # Prints 987
print(add(82, 746, 38, 392))    # Prints 1258
print(add(43, 3))   # Prints 46
