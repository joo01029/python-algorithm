def selectSort():
    array = [1,10,5,8,7,6,4,3,2,9]
    index = 0;
    for i in range(len(array)):
        min = 999999999
        for j in range(i, len(array)):
            if min > array[j]:
                min = array[j]
                index = j
        temp = array[i]
        array[i] = array[index]
        array[index] = temp;
    return array

print(selectSort())