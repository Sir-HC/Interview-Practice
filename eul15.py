#eul15

#we can at least cut the computation in half by only starting in one direction
#there's probably a tree structure in which we count leaf nodes, but it's not coming to me




def move(x, y):
    #print(str(x) + ' ' + str(y))
    if x == goal and y == goal:
        return 1
    elif x == 0:
        return move(x+1, y)
    elif x == goal and y < goal:
        return move(x, y + 1)
    elif x < goal and y == goal:
        return move(x+1, y) 
    else:
        return move(x + 1, y) + move(x , y + 1)



goal = 2
print(move(0,0) * 2)
goal = 3
print(move(0,0) * 2)
goal = 4
print(move(0,0) * 2)
goal = 5
print(move(0,0) * 2)
goal = 6
print(move(0,0) * 2)
goal = 7
print(move(0,0) * 2)

#Doesn't scale well, work of existing calculations
#If you reach an end point, record the number of ways you got to that end point
#check the catalogue

#Goal, find ways to get to each x=goal y=goal store in cata

def move_inc(x,y):
    #print(str(x) + ' ' + str(y))
    if x == goal and y == goal:
        catalogue[y][x] += 1
        return 1
    elif x == goal and y < goal:
        catalogue[y][x] += 1
        return move_inc(x, y + 1)
    elif x < goal and y == goal:
        catalogue[y][x] += 1
        return move_inc(x+1, y) 
    else:
        catalogue[y][x] += 1
        return move_inc(x + 1, y) + move_inc(x , y + 1)

def move_memo(index):
    catalogue[0][index] = 1
    catalogue[index][0] = 1
    for i in range(1,index+1):
        catalogue[i][index] = catalogue[i][index-1] + catalogue[i-1][index]
        catalogue[index][i] = catalogue[i][index]
        
    
def dis_mat(mat):
    print('matrix: =====')
    for y in range(goal):
        for x in range(goal):
            print(str(mat[y][x]) + ' ', end = '')
        print()
    print('==========')
# squares

goal = 21
catalogue = [[0] * (goal) for i in range(goal)]
catalogue[0][0] = 0
catalogue[0][1] = 1
catalogue[1][0] = 1
catalogue[1][1] = 2
for r in range(2, goal):
    move_memo(r)
dis_mat(catalogue)
print(catalogue[goal-1][goal-1])

input('exit')