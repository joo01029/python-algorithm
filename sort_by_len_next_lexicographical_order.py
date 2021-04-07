data = ["a", "asd", "bb", "b", "ab"]

def mergeSort(data):
    if len(data) <= 1:
        return data
    middle = len(data) // 2
    left = data[:middle]
    right = data[middle:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if len(left[0]) > len(right[0]):
                result.append(right[0])
                right = right[1:]
            elif len(left[0]) < len(right[0]):
                result.append(left[0])
                left =left[1:]
            else:
                if left[0] > right[0]:
                    result.append(right[0])
                    right = right[1:]
                else:
                    result.append(left[0])
                    left = left[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    return result

data = mergeSort(data)

print(data)