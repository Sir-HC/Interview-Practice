#eul01

import operator
from functools import reduce

numlist = range(1,(1000))

filt_list = list(filter(lambda x: ((x%5) == 0) or ((x%3) == 0), numlist))

print('filtered list:')
print(filt_list)

res = reduce(operator.add, filt_list)

print(res)

input('exit')