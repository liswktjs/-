def bubbleSort(data):
    #자리이동이 발생했을때, +1 씩 하여 자리이동을 한 횟수를 확인한다 
    swapHappenCount = 0
    #버블정렬은 한번 턴을 돌 때마다 정렬된 element를 제외하고  비고를 진행하기 때문에 이를 반영하기 위해서 2중 for문을 사용하여야 한다 
    #예를들어, 처음으로 한 바퀴를 돈 이후에는 마지막 자리에 위치한 element는 이미 해당 배열의 원소들 중 가장 큰 값이기 때문에 
    #두번째 턴을 돌 때에는 마지막 element와 그 앞의 element는 비교할 필요가 없다 

    #index는 0부터 시작한다 
    for index in range(len(data)-1):
        #자리이동이 발생했는지 확인하기 위한 변수 
        swap = False
        for index2 in range(len(data)- index - 1):
            #만약 앞에 위치한 원소가 뒤에 위치한 원소보다 값이 크면 서로 위치를 바꿔줘야한다 
            if data[index2] > data[index2 + 1 ]:
                data[index2], data[index2+1] = data[index2 + 1], data[index2]
                swap = True 
                #자리 이동이 발생했으므로 count를 올려 준다 
                swapHappenCount = swapHappenCount + 1

        #서로 비교하는 것이 모두 수행 되었음에도 불구하고 자리이동이 발생하지 않았다는 것은 
        #해당 배열은 이미 순서대로 배열이 되어있음을 의미한다 
        #그러므로 False일때는 더 이상 for문을 진행할 필요가 사라진다 
        if swap == False:
            break 

    #정렬된 결과를 확인 
    print (swapHappenCount," 번 자리이동이 발생했다. 정렬된 결과는 : ")
    for index3 in range(len(data) - 1):
        print (data[index3])

#예시 : {78,3,24,2,27,48,21}
data_list = list()
data_list.append(78)
data_list.append(3)
data_list.append(24)
data_list.append(2)
data_list.append(27)
data_list.append(48)
data_list.append(21)
bubbleSort(data_list )
    