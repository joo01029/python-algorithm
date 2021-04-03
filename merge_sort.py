data = [5,4,3,7,6,8,1,2,10,9,3,2,6,1,7,2]

def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    #중간을 기준으로 반 반 나눔
    leftList = list[:mid]
    rightList = list[mid:]
    print(leftList, rightList)
    #재귀로 반복
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)

    #머지로 두 리스트를 합침
    return merge(leftList, rightList)

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

print(merge_sort(data))