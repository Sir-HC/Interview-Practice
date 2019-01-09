#eul02

import operator
from functools import reduce

fib_one = 1
fib_two = 2

fib_target = 4000000

fib_list = [fib_one, fib_two]

print(str(len(fib_list)))
#while should keep running, this is a double stop-gap, cloud remove for improved performance
while(fib_list[len(fib_list)-1] <= fib_target):
    next_fib = fib_list[len(fib_list)-1] + fib_list[len(fib_list)-2]
    if next_fib <= fib_target:
        fib_list.append(next_fib)
    else:
        break
print('Fib list < target fib')    
print(fib_list)

filter_fib_list = list(filter(lambda x: x%2 == 0, fib_list))

print('Evens only: ')
print(filter_fib_list)

res = reduce(operator.add, filter_fib_list)

print('sum of evens')
print(res)

input('exit')