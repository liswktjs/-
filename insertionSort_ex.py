def insertSort(data):
    for index in range(len(data) -1):
        #비교 기준점이 되는 index 보다 하나 더 큰 index부터 배열의 맨앞의 원소까지 비교하기 위해서
        #index+1 부터 0까지 비교를 진행한다 그리고 역순으로 비교가 진행 되기 때문에 
        #-1씩 index2의 크기를 줄여주어야 한다 
        for index2 in range(index+1, 0, -1):
            #만일 앞에 있는 원소가 더 크다면 서로 위치를 바꿔줘야 한다 
            if data[index2] < data[index2 - 1]:
                data[index2], data[index2 - 1] = data[index2 - 1], data[index2]
            else:
                break 

    print("삽입정렬이 완료된 배열 결과: ")
    for index3 in range(len(data) -1):
        print(data[index3])


example_array = list()
example_array.append(456)
example_array.append(246)
example_array.append(365)
example_array.append(563)
example_array.append(112)
example_array.append(2)
example_array.append(222)

insertSort(example_array)