def selectSort(data_list):
    #기준이 되는 기점을 중심 (첫번째 수행시 0번 element 두번째 시행시 1번 element...)
    #과 나머지 원소들을 모두 비교해서 기준이 되는 원소보다 더 값이 작은 원소가 있을 경우에 
    #기준이 되는 자리의 원소와 더 값이 작은 원소의 자리를 바꿔준다 
    for index in range(len(data_list) - 1):
        #비교 기준이되는 index를 lowest 변수에 임시로 저장한다 
        lowest = index
        #비교 기준이 되는 원소의 바로 다음 원소부터 비교를 진행한다 
        #비교가 완료된 원소는 다음 선택정렬 과정에서 배제 되므로 
        #for문을 2번 반복하여 차례대로 배열이 완료된 원소를 배제시키며 진행한다 
        for index2 in range(index + 1, len(data_list)):
            #만일 기준이 되는 원소보다 다른 원소가 더 작을 때 두 원소는 서로 자리를 바꾼다 
            if data_list[lowest] > data_list[index2]:
                lowest = index2 
                data_list[lowest], data_list[index] = data_list[index], data_list[lowest]

    print("선택정렬이 된 결과: ")
    for index3 in range(len(data_list)):
        print(data_list[index3])

#예시 배열 {356, 584, 232, 21, 654, 1}
example_array = list()
example_array.append(356)
example_array.append(584)
example_array.append(232)
example_array.append(21)
example_array.append(654)
example_array.append(1)

selectSort(example_array)
