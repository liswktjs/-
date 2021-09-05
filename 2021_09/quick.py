#퀵정렬의 진행 순서 
#피봇 즉 기준점을 배열의 첫번째 원소로 정하고, left노드는 pivot의 다음 원소 그리고 right노드는 배열의 마지막 원소로 정한다 
#left는 pivot보다 크거나 같은 값을 찾으면 멈추고, right는 pivot보다 작은 값을 찾으면 탐색을 멈춘다
#그 후 left와 right의 노드위 위치를 서로 바꾸어준다  
#만약 탐색을 계속 진행해 나가다가 left와 right가 서로 엇갈리게 되면 pivot과  right가 가리키는 곳을 서로 바꾼다 
#이때에 피봇을 기준으로 왼쪽에는 피봇보다 작은 값들이 위치하고 오른쪽에는 피봇보다 큰 값들이 위치하게 된다 
#피봇을 기준으로 분할하여 분할된 리스트끼리 다시 같은 작업을 반복한다 

def quickSort(array, start, end):
    if len(array) < 2:
        return 

    pivot_index = start
    left_index = start+ 1
    right_index = end 
    while left_index <= right_index:

        for i in range(len(array)):
            if array[left_index] >= array[pivot_index]:
                left_index = i
                break
        for j in range(end, start+1, -1):
            if array[right_index] < array[pivot_index]:
                right_index = j
                break
        if array[left_index] > array[right_index]:
            left_index, right_index = right_index, left_index

        if left_index == right_index:
            right_index, pivot_index = pivot_index, right_index

    quickSort(array, start, right_index-1)
    quickSort(array, right_index+1 , end)

        

    
data = [69, 10, 30, 2, 16, 8 ,31 ,22]
print(quickSort(data, 0 , len(data) -1))
print(data)