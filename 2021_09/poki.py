#떡볶이 떡 만들기 문제
#난이도 2.0  소요시간 15분 

n,m = map(int,input().split())

data = list(map(int,input().split()))

data = sorted(data, reverse=True)

def cut (array, t,m):
    datasum = 0
    for item in array:
        if item - t > 0:
            datasum += (item - t)

    if datasum >= m:
        return True
    else:
        return False

    return True
for i in range(data[1], 0, -1):
    if cut(data,i,m):
        print(i)
        break

#이진 탐색을 활용한 답안

start = 0 
end = max(data)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in data:
        if x > mid:
            total += x - mid
    if total < m :
        end = mid - 1
    
    else:
        result = mid
        start = mid + 1

print(result)