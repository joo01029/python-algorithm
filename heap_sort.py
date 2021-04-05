heap = [3,2,5,4,1,6,8,0,7,9]

def HeapFindBigger(i, root):
    c = 2 * root +1
    if c < i -1 and heap[c] < heap[c+1]:
        c+=1

    if c < i and heap[root] < heap[c]:
        temp = heap[root]
        heap[root] = heap[c]
        heap[c] = temp

    return c

def HeapFirst(c):
    root = int((c - 1) / 2)
    if heap[root] < heap[c]:
        temp = heap[root]
        heap[root] = heap[c]
        heap[c] = temp
    return root

def main():
    for i in range(1,len(heap)):
        c = i
        c = HeapFirst(c)
        while c!=0:
            c=HeapFirst(c)

    for i in range(len(heap)-1, -1,-1):
        temp = heap[0]
        heap[0] = heap[i]
        heap[i] = temp

        root = 0
        c = HeapFindBigger(i, root)
        root = c
        while (c < i):
            c = HeapFindBigger(i, root)
            print(heap)
            root = c

    print(heap)