import heapq
import sys 
input = sys.stdin.readline
#무한을 의미하는 값을 10억으로 설정 
INF = int(1e9)

#노드의 개수, 간선의 개수를 입력받기 
n,m = map(int, input().split())
#시작 노드의 번호를 입력 받기 
start = int(input())
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만든다 /리스트 안에 리스트
graph = [[] for i in range(n+1)]
#최단 거리 테이블을 모두 무한으로 초기화한다 
distance = [INF] * (n+1)

#모든 간선 정보에 대해서 입력받는다 
for _ in range(m):
    a, b, c = map(int, input().split())
    #a 노드에서 b 노드로 가는 비용(=가중치,거리)가 c이다 
    graph[a].append((b,c))

def dijkstra(start):
    # 큐 생성
    q = []
    # 시작 노드의 경우 자기 자신에게 가는 거리는 0이므로, 시작노드에 대한 초기화를 해준다
    heapq.heappush(q, (0,start))
    distance[start] = 0

    #큐에 원소가 있을 경우에만 while문 안의 작업들을 수행한다 
    while q:
        # 최단거리 노드에 대한 정보를 꺼낸다 (우선순위 큐이므로 최단 거리 노드가 pop이 된다)
        dist, now = heapq.heappop(q)
        # pop이 된 거리가 원래의 최단 거리 보다 큰 경우 계산을 스킵한다 
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 노드들의 거리를 확인한다 
        for i in graph[now]:
            # 현재 노드에서 다른 노드를 거쳐서 갈 때의 비용 
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드까지 이동하는 거리가 짧을 경우 
            # 최단 거리를 update를 해준다 
            if cost < distance[i[0]]:
                # i[0] 즉, 앞 부분이 b 임을 헷깔리지 말자 
                distance[i[0]] = cost 
                heapq.heappush(q,(cost,i[0]))


dijkstra(start)

#모든 노드로 가기 위한 최단 거리를 출력한다 
for i in range(1, n+1):
    # 노드간에 연결되어 있지 않은 경우 무한으로 거리를 표현한다 
    if distance[i] == INF:
        print("INFINITY")
    # 아닌 경우, 계산한 거리를 출력 
    else: 
        print(distance[i])
