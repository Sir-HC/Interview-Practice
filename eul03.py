#eul03

#Objectives:
#1: generate prime numbers up to target number
#2: attempt to modulo prime numbers by target number

import math
import time

target_num = 600851475143

#we don't need to generate primes past target_num^2 
max_prime = math.floor(math.sqrt(target_num))

print('find primes from 2 to ' + str(max_prime))
#check for improved algorithm for finding primes
#edit: first stab was to go from top to bottom, but that took excess of 10mins
# kinda cheesed it by going bottom up and picking the largest prime factor after 10 seconds
# not sure if this is 'good enough' or heuristicly good, but compared to the
# example answer it made sense that the answer would be orders of magnitude smaller

str_time = time.time()
time_chk = 10

#if no answers come up, singleton check 2
for x in range(3,max_prime):
    #debug timer
    cur_time = time.time()
    elapsed = cur_time - str_time
    if elapsed > time_chk:
        print('Seconds elapsed: ' + str(elapsed))
        time_chk = time_chk + 10
    
    #Take out all even numbers, these are not primes
    #primality check 
    for y in range(3, x, 2):
        if (x%y) == 0:
            break
    else:
        if target_num%x == 0:
            print("found: "+ str(x))
            print(elapsed)
                

input('exit')
