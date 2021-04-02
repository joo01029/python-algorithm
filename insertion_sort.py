def insertionSort():
    array = [1,10,5,8,6,7,3,2,4,9]
    for i in range(len(array)-1):
        j = i;
        while(array[j]> array[j+1]):
            temp = array[j+1]
            array[j+1] = array[j]
            array[j] = temp
            j-=1

    return array

print(insertionSort())