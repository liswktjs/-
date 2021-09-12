INF = int(1e9)

#노드의 개수, 간선의 개수 입력받기
n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

#자기 자신에게 가는 거리 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

#간선에 대한 정보를 입력받아, 그 값으로 초기화

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+ graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("infinity",end= " ")
        else:
            print(graph[a][b], end=" ")

    print()