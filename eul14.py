#eul14


def next_chain(num):
    #num is even, do n/2
    if num %2 == 0:
        num = num/2
    else:
        num = 3*num+1
    return num

max = 0
for i in range(999999, 1, -2): #don't bother with evens, it's a dead start 
    res = i
    increments = 0
    while res != 1:
        res = next_chain(res)
        increments += 1
    if increments > max:
        max = increments
        print("val: " + str(i) + " increments: " + str(increments))