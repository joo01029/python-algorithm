number = 6
inf = 1000000000

a = [[0,2,5,1,inf,inf],
     [2,0,3,2,inf,inf],
     [5,3,0,3,1,5],
     [1,2,3,0,1,inf],
     [inf,inf,1,1,0,2],
     [inf,inf,5,inf,2,0]]

v = [False for i in range(6)]
d = [0 for i in range(6)]

def getSmall():
    min = inf
    index = 0
    for i in range(number):
        if d[i] < min and (not v[i]):
            min = d[i]
            index = i
    return index

def dijkstra(start):
    for i in range(number):
        d[i] = a[start][i]

    v[start] = True
    for i in range(number -2):
        current = getSmall()
        v[current] = True

        for j in range(number):
            if not v[j]:
                if d[current] + a[current][j] < d[j]:
                    d[j] = d[current]+a[current][j]

dijkstra(0)

print(d)