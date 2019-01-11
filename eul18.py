#eul18

class node:
    def __init__(self, index, val, **keyargs):
        if('left' in keyargs):
            self.left = keyargs['left']
        if('right' in keyargs):
            self.right = keyargs['right']
        self.index = index
        self.val = val

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node
    
    

_in = ['75','95 64','17 47 82','18 35 87 10','20 04 82 47 65','19 01 23 75 03 34','88 02 77 73 07 63 67','99 65 04 28 06 16 70 92','41 41 26 56 83 40 80 70 33','41 48 72 33 47 32 37 16 94 29','53 71 44 65 25 43 91 52 97 51 14','70 11 33 28 77 73 17 78 39 68 17 57','91 71 52 38 17 14 91 43 58 50 27 29 48','63 66 04 68 89 53 67 30 73 16 69 87 40 31','04 62 98 27 23 09 70 98 73 93 38 53 60 04 23']
tree = []
for x in _in:
    #print(x)
    tree.append(x.split())
print(tree)

_items = 0

def gen_tree(y,x):
    print('y ' + str(y) + ' x ' + str(x))
    global _items
    print('Created: ' + str(_items))
    if _items > 200:
        return
    
    if y < len(tree) - 1:
        #if x == 0:
            #node can create unshared left
            
        
        print('node made')
        _items += 1
        _left = gen_tree(y+1,x)
        #_right = gen_tree(y+1,x+1)
        
        return node(tree[y][x], left= _left )
    else:
        _items += 1
        print('leaf made')
        return node(tree[y][x])
    
node_list = []
idx = 0
for y in range(len(tree)):
    for x in range(len(tree[y])):
        node_list.append(node(idx, tree[y][x]))
        idx += 1

print(node_list)
index = 0
adj_i = 1
for y in range(len(tree)-1):
    
    for x in range(len(tree[y])):
        print('node: ' + str(index))
        print('adj: ' + str(adj_i), end= '')
        
        node_list[index].set_left(node_list[adj_i])
        adj_i += 1
        print(' and ' + str(adj_i))
        node_list[index].set_right(node_list[adj_i])
        index += 1
    
    adj_i += 1

def print_graph(gra):
    print(gra.index)
    print(gra.val)
    
    print_graph(gra.left)
    
head = node_list[0]  
print_graph(head)



input('exit')