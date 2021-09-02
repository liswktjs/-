n, m = map(int,input().split())
data = [list(map(int,input().split()))for _ in range(n)]

min_list = list()
min = 10001
max = 0

for i in range(n):
    for j in range(m):
        if data[i][j] < min :
            min = data[i][j]
    
    min_list.append(min)
    min = 10001

for i in range(n):
    if max < min_list[i]:
        max = min_list[i]

print (max)
