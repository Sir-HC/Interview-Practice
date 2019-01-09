#eul04

#objectives:
#1: meta analysis: max number possible is 999*999 = 998001 so obviously we are looking for a palindrome of 6 digits
#2: it's faster to analyse from top to bottom on this, rercursive call tree find_pal(x, y-1) | find_pal(x-1, y-1)?
import sys
import time

sys.setrecursionlimit(1500)
#edit: recursive was too deep for python, unsure of stability in higher numbers, switching to iterative approach


memo = [];

def is_pal(x):
    #print('check pal: ' +str(x))
    str_x = str(x)
    rev_x = str_x[::-1]
    if str_x == rev_x:
        return True
    else:
        return False

def find_pal(x, y):
    chk = x * y
    print("x: " + str(x))
    print("y: " + str(y))
    concat = int(str(x) + str(y))
    invconcat = int(str(y) + str(x))
    if is_pal(chk):
        return chk
    
    elif (not concat in memo) or (not invconcat in memo): 
        memo.append(concat)
        return (find_pal(x-1, y) | find_pal(x, y-1))
    return

highest = 0
    
#right now this is bad, it would be great if we could alternate reduction in x then y
#we could do some sort of short increment like 100 to check to increase speed, but alternating
#would be the biggest performance gains
#Still runs in less than a second (~.63s)

str_time = time.time()

for x in range(999,0, -1):
    for y in range(999, 0, -1):
        mul = x*y
        if is_pal(mul) and mul > highest:
            print(str(x) + " x " + str(y) + " = " + str(mul))
            highest = mul

end_time = time.time()
print(end_time - str_time)
input('exit')