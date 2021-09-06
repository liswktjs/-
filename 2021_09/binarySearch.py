#이진탐색 알고리즘 

array = [1,2,3,4,5,6,7,8,9,10]

#찾고자 하는 데이터 7

def binarySearch(array, t,start, end):
    start = start
    middle = (start + end) // 2
    end = end
    target = t

    if array[middle] == target:
        return middle

    elif array[middle] < target:
        return binarySearch(array,target,middle+1, end)
    else:
        return binarySearch(array, target,start, middle-1)

print(binarySearch(array, 7, 0, len(array) -1))

