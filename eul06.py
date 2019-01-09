#eul06

#sum of squared by map reduce, square of sums by adding and performing a square

import operator
from functools import reduce
import math


#map reduce, good performance gains if used with hadoop
_range = range(1,100 + 1)
#print(list(_range))
#print(list(map(lambda x: int(math.pow(x, 2)), _range)))
sOfSquares = reduce(operator.add, map(lambda x: int(math.pow(x, 2)), _range))

print(str(sOfSquares))
sqOfSums = int(math.pow(reduce(operator.add, _range),2))

print(str(sqOfSums))
print(str(sqOfSums - sOfSquares))

input('exit')


