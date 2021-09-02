# 동전문제 
# 4720원일 때, 1원 50원 100원 500원 동전으로 동전 수가 가장 적게 지불하시오 

coin_list = [500,100,50,10]

def min_coint_count(value,coin_list):
    #총 동전의 수를 구하기 위한 변수 
    coin_count = 0
    #각각의 동전이 얼마씩 쓰였는지 알아보기 위한 리스트
    coin_details= list()
    #coin_list에서 큰 수 부터 앞에 오게 하기 위해서 
    #sort 함수에 reverse=True를 해준다 
    coin_list.sort(reverse=True)

    #coin_list의 있는 원소중 500원부터 시작해서, 
    #몫을 통해 몇개의 동전이 쓰였는지 구한다 
    for coin in coin_list:
        #총 금액에 coin원소를 나누면 나오는 몫은
        #해당 coin 원소가 그만큼 쓰일 수 있음을 의미한다 
        coin_num = value // coin
        #쓰인 동전의 갯수 만큼 coin_count를 업데이트 해준다
        coin_count += coin_num
        #쓰인 동전 만큼은 총액에서 감해진것이기 때문에 
        #갯수 * 동전 금액 만큼을 빼준다 
        value -= coin_num * coin 
        #얼마만큼의 금액이 쓰였는지 알기 위해서 
        #동전의 종류와 갯수를 리스트에 추가해준다 
        coin_details.append([coin,coin_num])

    #총 사용된 동전의 갯수를 반환한다 
    return coin_count, coin_details

print(min_coint_count(4720,coin_list))

# 4720 = 500 * 9 + 100 * 2 + 50 * 0 + 10 * 2 