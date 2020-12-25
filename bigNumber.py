n,m,k = map(int, input().split()) 
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = 0 
result = 0

while True :
    if count == m:
        break 
    temp = k
    while temp != 0 :
        if count == m:
            break
        result = result + first
        count = count + 1
        temp = temp -1

    result += second
    count = count + 1


print(result)