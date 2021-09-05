#위에서 아래로 
#난이도 1.0

n = int(input())
array = list()
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
    print(i , end=' ')

