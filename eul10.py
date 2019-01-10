#eul10

import operator
from functools import reduce
import time
import math

#function kinda sucks, get the answer in 22s, others get 3s or less
def gen_primes(max):
    primes = [2]
    for x in range(3, max):
        for y in primes:
            #if x is divisible by a prime, it's not prime
            if x%y == 0:
                break
            #don't check numbers past the square of a given prime 
            #(the high end of a potential discovered prime is a multiple of itself)
            if y > math.floor(math.sqrt(x)):
                primes.append(x)
                break
    return primes 
    
    
#alternate solution for experimenting
def sieve(upper_limit):
    """Returns a list of prime numbers within the range [2, n) using Sieve of Eratosthenes"""
    primes = [True for i in range(upper_limit)]

    i = 2
    while i < math.sqrt(upper_limit):
        if primes[i]:
            k = 0
            j = i**2 + k*i
            while j < upper_limit:
                primes[j] = False
                k += 1
                j = i**2 + k*i
        i += 1

    primes = [i for i in range(2, upper_limit) if primes[i]]

    return primes
    
 
def sieve_i(upper_limit):
    """Returns a list of prime numbers within the range [2, n) using Sieve of Eratosthenes"""
    primes = [True for i in range(upper_limit)]

    false_flags = 0
    i = 2
    while i < math.sqrt(upper_limit):
        if primes[i]:
            k = 0
            #removed unessisary multiplication /addition
            j = i**2
            #if number is prime, every multiple of it should be marked as false
            #optimization would be to try and stop multiple flaggings
            while j < upper_limit:
                primes[j] = False
                #false_flags += 1
                k += 1
                j = i**2 + k*i
        i += 1

    print("false switches: " + str(false_flags) + " out of " + str(len(primes)))
    primes = [i for i in range(2, upper_limit) if primes[i]]

    return primes 
 
_ui = int(input('prime max out: \n'))

str_time = time.time()

_primes = sieve(_ui)
#print(_primes)
res = reduce(operator.add, _primes)
print(res)

end_time = time.time()
print("time taken: " + str(end_time - str_time) + "s")
#=======================


str_time = time.time()

_primes = sieve_i(_ui)
print(_primes)
res = reduce(operator.add, _primes)
print(res)

end_time = time.time()
print("time taken: " + str(end_time - str_time) + "s")




input('exit')