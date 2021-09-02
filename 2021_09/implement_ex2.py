#구현문제 예제 2
#시각 소요시간 10분 12초

n = int(input())

s = 0 
m = 0
h = 0

count = 0 

while True:
    if h > n:
        break 
    s += 1 
    if s > 59:
        m += 1
        s = 0
    if m > 59:
       h += 1
       m = 0 

    if '3' in str(h) or '3' in str(m) or '3' in str(s):
        count += 1

print(count)

# 해설 
'''
시간은 60분을 단위로 하므로 for 문을 통해서 간단하게 루프를 돌 수 있다 
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1 
'''