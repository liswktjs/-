# 두 배열의 원소 교체 
# 난이도 1.0 소요시간 8분

n,k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

b = sorted(b, reverse=True)
a.sort()

for i in range(k):
    a[i], b[i] = b[i], a[i]

print(sum(a))