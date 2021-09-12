#미래도시문제
#난이도 2.0 소요시간 1시간 20분
import heapq

n, m = map(int,input().split())

INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

#연결된 정보 입력 
#저장되는 정보 양식 : a(출발노드) b(도착노드) 
for _ in range(m):
    a, b = map(int,input().split())
    #2차원배열 
    graph[a][b] = 1
    graph[b][a] = 1

x,k = map(int,input().split())

#a와 b를 순회하면서는 해당 노드간의 최소 거리를 update하고
#k를 통해서는 특정 k번 노드를 지나쳤을때의 거리 weight를 구해서 최소값으로 update해준다
for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)



