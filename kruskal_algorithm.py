def getParent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = getParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def findParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a == b:
        return True
    else:
        return False

class Edge:
    def __init__(self,a,b,distance):
        self.node = [a,b]
        self.distance = distance

    def operator(selt, edge):
        return self.distance < edge.distance

n = 7
m = 11

v = []
v.append(Edge(1,7,10))
v.append(Edge(1,4,28))
v.append(Edge(1,2,67))
v.append(Edge(1,5,17))
v.append(Edge(2,4,24))
v.append(Edge(2,5,62))
v.append(Edge(3,5,20))
v.append(Edge(3,6,37))
v.append(Edge(4,7,131))
v.append(Edge(5,6,45))
v.append(Edge(5,7,73))

v.sort(key=lambda edge:edge.distance)

parent = [i for i in range(0, n)]

sum = 0
for i in range(len(v)):
    if not(findParent(parent, v[i].node[0]-1, v[i].node[1]-1)):
        sum += v[i].distance
        unionParent(parent, v[i].node[0]-1, v[i].node[1]-1)

print(parent)


print(sum)