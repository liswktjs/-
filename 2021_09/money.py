#효율적인 화폐 구성
#난이도 2.0 

n,m = int(input().split())

coin = []
for i in range(n):
    coin.append(int(input()))

d = [0] * 101
