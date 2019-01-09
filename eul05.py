#eul05

#Objectives:
#1: number must be even, attempts should be made with prime numbers, probably highest prime number?
#2: attempt to use multiples of highest prime number of 1-20 (19), multiplied by 2 to meet obj1, attempt to check from highest to lowest, or maybe primes then highest to lowest?

import time
#this really quick solution takes a bit to solve, but it gets the job done
# ~3.5 seconds
str_time = time.time()
index = 20
val = 19

while index > 0:
    if val%index == 0:
        index = index - 1
    else:
        index = 20
        val = val + 19
        
end_time = time.time()
print(val)
print('Time: ' + str(end_time - str_time))
