# 개미전사 
# 난이도 2.0 소요시간 12분 
import random
n = int(input())

#k = list(map(int,input().split()))

k = list()
for i in range(0, n):
    k.append(random.randint(0,1001))


d1 = [0] * 101

d1[0]= k[0]
d1[1]= k[1]

for i in range(2, n):
    d1[i] = d1[i-2]  + k[i]       

d2 = [0] * 101
d2[0] = k[0]
d2[1] = max(k[0],k[1])

for i in range(2, n):
    d2[i] = max(d2[i-1], d2[i-2] + k[i])

print(k)
print(d1[0: 10])
print(d1[n-1], d1[n-2], d2[n-1])
result = max(d1[n-1], d1[n-2], d2[n-1])
print(result)