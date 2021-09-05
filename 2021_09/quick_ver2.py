def quickSort(data_list):
    
    if len(data_list) <= 1:
        return data_list
    
    left_list = list()
    right_list = list()
    
    pivot = data_list[0]
    
    for index in range(1, len(data_list)):
        if pivot > data_list[index]:
            left_list.append(data_list[index])
        else:
            right_list.append(data_list[index])
    return quickSort(left_list) + [pivot] + quickSort(right_list)

data = [5,7,9,0,3,1,6,2,4,8]

print(quickSort(data))