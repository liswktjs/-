def mergeSplit(data_list):
    #배열의 길이가 1 이하이면 정렬을 할 필요가 없으므로 그대로 배열을 반환한다
    if len(data_list) <= 1:
        return data_list
    
    #배열을 나눠야 하기 때문에 기준 점을 배열의 중앙 원소로 잡아 배열을 나눈다 
    middle = int(len(data_list)/2)

    #배열을 나눌때, 함수를 재귀적으로 호출 함으로써, 
    #해당 배열의 원소가 하나가 될때 까지 split이 진행된다 
    #0부터 middle 이전 원소까지 left_list로 배당한다
    left_list = mergeSplit(data_list[:middle])
    #middle 부터 배열의 마지막 원소까지 right_list로 배당한다 
    right_list = mergeSplit(data_list[middle:])

    #나누어진 원소가 mergeSort함수에 하나씩 배당이 된다 
    #해당 코드에서는 원소가 하나인 배열부터 하나씩, 호출이 된다 (쌓여있는 명령들이 하나씩 pop된다)
    return mergeSort(left_list, right_list)

def mergeSort(left_list,right_list):

    #left_list 와 right_list를 비교를 통해서 순서대로 원소를 합칠 배열을 만든다
    merged_list = list()

    #left_list와 right_list 들 중 각각 비교 대상이 되는 원소를 가리키기 위한 인덱스 
    #처음부터 비교하기 위해서 0부터 시작한다 
    left_point, right_point = 0, 0

    #list의 길이보다 point의 크기가 더 클 때, 더이상 배열을 할 것이 없다는 의미이다 
    #그러므로, while은 point의 크기가 list의 크기보다 작을 때에만 진행된다 

    #case1 : left_list, right_list가 아직 남아있을 때 
    #= left_list와 right_list 모두 아직 정렬을 해야할 원소들이 남아있을 때 
    while len(left_list) > left_point and len(right_list) > right_point :
        #left_list의 left_point가 가리키는 원소가 right_list의 right_point가 가리키는 
        if left_list[left_point] > right_list[right_point]:
            #right의 원소가 먼저 merged_list 배열에 배당이 되어야 한다 
            merged_list.append(right_list[right_point])

            #right_list의 원소는 배당이 되었으므로, 다음 원소를 가리키기 위해서, 
            #right_point 인덱스를 업데이트 해준다 
            right_point += 1 

        else:
            #left의 원소가 더 작을때, left의 원소를 배당해준다 
            merged_list.append(left_list[left_point])
            #left_point의 인덱스를 업데이트 해준다 
            left_point += 1
    
    #case2: right_list의 원소들이 정렬이 모두 완료되어 left_list의 원소들만이 남았을 때 
    while len(left_list) > left_point:
        #left_list는 이미 정렬이 완료된 리스트이기 때문에  left_list의 남은 원소들을 
        #차례대로 merged_list에 배당한다 
        merged_list.append(left_list[left_point])
        #다음 원소를 가리키기기 위해서 left_point 인덱스를 업데이트 해준다 
        left_point += 1

    #case3 : left_list의 원소들이 정렬이 모두 완료되어 right_list의 원소들만이 남았을 때
    while len(right_list) > right_point:
        #right_list의 원소들은 이미 순서대로 정렬이 되어 있기 때문에 순서대로 
        #merged_list에 배당한다 
        merged_list.append(right_list[right_point])
        #다음 원소를 가리키기 위해서 right_point 인덱스를 업데이트 해준다 
        right_point += 1 

    #나누어졌던, left_list와 right_list의 원소를 비교를 통해서 정렬이 완료된 list를 반환해준다 
    return merged_list

#확인용 예시 
import random

data = random.sample(range(100),10)
print(data)
print("mergeSort 된 후 배열:")
print(mergeSplit(data))

