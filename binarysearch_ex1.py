def binarySearch(data_list , target):

    #data_list가 원소를 가지고 않은 상태이므로 False를 반환한다 
    if len(data_list) == 0:
        return False
    #data_list의 길이가 1이면서 첫번째 원소가 찾고자 하는 target가 아닐때
    #list의 모든 원소를 검색해봐도 target이 없는 것이므로 False를 반환한다 
    if len(data_list) == 1 and data_list[0] != target:
        return False

    #가운데 있는 항목과 찾고자 하는 target을 비교해야하므로 
    #middle 의 인덱스를 data_list의 길이를 2로 나눈 몫으로 정한다 
    middle = int(len(data_list)//2)

    #middle값과 target이 같다면, data_list에 target값이 있는 것이므로, 
    #return True를 해준다 
    if data_list[middle] == target:
        return True
    else:
        #중앙값(=middle값)이 target보다 크다면, 중앙값을 기준으로 왼쪽 리스트에 target값이 있으므로
        # data_list를 middle을 기준으로 인덱스 0부터 middle 이전의 수까지로 업데이트 해준다
        if data_list[middle] > target:
            return binarySearch(data_list[:middle],target)
        #중앙값이 target보다 작다면, 중앙값을 기준으로 오른쪽 리스트에 target 값이 있으므로 
        #data_list를 middle를 기준으로 middle 다음값 부터 마지막 원소까지로 업데이트 해준다 
        else:
            return binarySearch(data_list[middle:],target)

#예시 
import random
data_list = random.sample(range(100),10)
# 이진탐색을 하기 위해서는 data_list가 사전적으로 정렬이 되어야 되기 때문에 
# data_list를 정렬해준다 
data_list.sort()
print(data_list)
#data_list의 값 중에서 임의로 값을 지정해서, 찾을 수 있는지 확인한다
target1 = data_list[0]
print(binarySearch(data_list, target1))
#배열에 없는 값을 지정해서, 올바르게 판단할 수 있는지 확인한다 
target2 = 13
print(binarySearch(data_list, target2))
        