#부분 배낭 문제 (Fractional knapsack Problem)
#무게 제한이 k 인 배낭에 최대 가치를 가지도록 물건을 넣는 문제
#물건을 쪼갤 수 있으므로 물건의 일부분이 배낭에 넣어질 수 있음 
#물건리스트  1  2   3   4   5
# 무게      10  15  20  25  30
# 가치      10  12  10  8   5

data_list = [(10,10),(15,12),(20,10),(25,8),(30,5)]

def knapsack(k,data_list):
    #가치를 무게로 나눈 것을 기준으로 data_list를 정렬한다 
    #=무게 대비 가치가 높은 순으로 정렬이 되게 된다 
    data_list = sorted(data_list, key=lambda x:x[1]/x[0], reverse=True)
    #배낭안에 있는 물건들의 전체 가치
    total_value = 0 
    #어떤 물건들이 들어가 있는지 표시할 리스트 
    details_list = list()

    for data in data_list:
        #배낭에 들어갈 수 있는 무게가, 물건리스트의 물건보다 더 크다
        if k - data[0] >= 0:
            #해당 물건이 들어갔으므로 물건만큼의 무게를 배낭의 무게에서 빼준다 
            k -= data[0]
            #전체 가치 value에 해당 물건의 가치를 더해준다 
            total_value += data[1]
            #해당 물건이 배낭에 들어갔으므로, 어떤 물건이 들어가 있는지 표시하는 리스트에 업데이트한다
            details_list.append([data[0],data[1],1])

        #넣어야할 물건의 무게가 배낭에 들어갈 수 있는 무게보다 클 때에,
        #물건을 분할하여 배낭에 넣어야 한다 
        else:
            #나눠 담아야 할 무게를 구하기 위해서 남은 배낭 무게에서 
            #넣고자 하는 물건의 무게를 나눈다 
            fraction = k / data[0]
            #전체 가치는 들어간 만큼의 무게만큼의 가치만 들어가 있으므로 
            #fraction 비율을 곱해준다 
            total_value += data[0] * fraction
            #해당 물건은 들어 갔으므로, 어떤 물건이 들어가 있는지 리스트에 표시해준다 + 비율도 
            details_list.append([data[0],data[1],fraction])
            #배낭의 남은 무게만큼 물건을 넣은 것이기 때문에, 배낭에는 더이상 넣을 곳이 없다 
            break
        
    return total_value, details_list


print(knapsack(40, data_list))