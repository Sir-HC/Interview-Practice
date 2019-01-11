#eul16

from functools import reduce
#2 = 2^1, we need to add 999 more 
num = 2

#NOTE this is only for powers of 2
power = 2 << 999

print(reduce(lambda acc, x: acc + int(x), list(str(power)),0))


input('exit')