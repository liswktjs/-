def quickSort(data_list):
    #배열의 원소가 1개 이하이므로 정렬을 진행할 필요가 없다 
    if len(data_list) <=1:
        return data_list

    #pivot을 중심으로 원소들을 분류하여 배치시킬 배열을 생성한다 
    left_list = list()
    right_list = list()

    #pivot을 배열의 맨 앞의 원소로 정하고 시작한다 
    pivot = data_list[0]

    #pivot인 원소(=0번째 원소)의 다음 원소(=1)부터 비교의 대상으로 시작한다 
    for index in range(1,len(data_list)):
        #pivot 보다 작은 원소는 left_list에 배당한다
        if pivot > data_list[index]:
            left_list.append(data_list[index])
        #pivot 보다 크거나 같은 원소는 right_list에 배당한다
        else:
            right_list.append(data_list[index])
    
    #각각, 배열이 완료된 list들과 pivot 원소를 합치면 정렬이 완료된 배열이 완성된다
    return quickSort(left_list) + [pivot] + quickSort(right_list)


#코드를 검증하기 위한 예시 
import random 

data = random.sample(range(100),6)
print(data)
print("정렬결과:")
print(quickSort(data))
