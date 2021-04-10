a = {1:set([3,4]),
     2:set([3,4,5]),
     3:set([1,5]),
     4:set([1]),
     5:set([2,6]),
     6:set([3,5])}

visited = []

def DFS(x):
    if not(set([x]) - set(visited)):
        return
    visited.append(x)
    for i in a[x]:
        DFS(i)

DFS(3)

print(visited)