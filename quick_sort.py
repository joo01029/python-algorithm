number = 10
data = [2,10,5,8,7,6,4,3,1,9]

def quickSort(start, end):
    if start >= end:
        return

    key = start
    i = start +1
    j = end

    while i <= j:
        while(data[j] <= data[key] and j > start):
            j-=1

        while(data[i] >= data[key] and i <= end):
            i+=1
            if( i > end):
                break

        if i > j:
            temp = data[j]
            data[j] = data[key]
            data[key] = temp

        else:
            temp = data[j]
            data[j] = data[i]
            data[i] = temp

    quickSort(start, j-1)
    quickSort(j+1, end)


quickSort(0, number-1)

print(data)