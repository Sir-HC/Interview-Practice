#eul07


import time
target_prime_index = 10001
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


#init suggests we have 2 as the first prime index, start at 3, increment by 2, evens except 2 arnt prime
#edit; This chugs for a while but it gets it done without an advanced heruristics algorithm
# 70.16s before is_prime optimization
# 34.30s after is_prime optimization (increment by 2's)
str_time = time.time()

while target_prime_index > cur_prime_index:
    if is_prime(cur):
        cur_prime_index = cur_prime_index + 1
        cur_prime = cur
    cur = cur + 2

end_time = time.time()
print('Cur prime index: ' + str(cur_prime_index))
print('cur prime: ' + str(cur_prime))
print('time taken: ' + str(end_time - str_time))