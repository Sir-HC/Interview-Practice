#test

import sys

x = 3294

bytes = sys.getsizeof(x)

bits = bytes * 8

acc = 0
for i in range(bits):
    print('x: ', end = '')
    print(x)
    if x and 1:
        acc += 1
    x = x >> 1
print('acc: ' + str(acc))

#print(sys.getsizeof(x))

#print(type(x))

input('exit')