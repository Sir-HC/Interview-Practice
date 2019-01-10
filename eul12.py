#eul12

import math
from functools import reduce 
import operator


#we want the lowest(first) value that gives us 500 divisors

#divisors = exponent(s) + 1 of each prime divisors

#2^499 huge
#2^
#2^22 * 3^22            43873901280755712
#2^7 * 3^7 * 5^7        43740000000
#2^4 * 3^4 * 5^4 * 7^3  277830000

target_prime_index = 500
cur_prime_index = 1
cur_prime = 2
cur = 3

def is_prime(x):
    if x%2 == 0:
        return False
    for i in range(3, x, 2):
        if x%i == 0:
            return False
    return True

prime_list = []
while target_prime_index > cur_prime_index:
    if is_prime(cur):
        prime_list.append(cur)
        cur_prime_index = cur_prime_index + 1
        cur_prime = cur
    cur = cur + 2

print(reduce(operator.mul, prime_list))

    
def gen_tri_nums(index):
    tri = [0]
    for i in range(1, index):
        if i == 1:
            tri.append(1)
        else:
            tri.append(tri[i-1] + i)
    return tri
    
_list = gen_tri_nums(3000)

ref_list = []
for x in _list:
    if x%2 ==0:
        ref_list.append(x)

print(ref_list)        
input('exit')