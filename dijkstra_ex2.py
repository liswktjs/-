import sys
input = sys.stdin.readline
#무한대의 값을 10억으로 설정한다 
INF = int(1e9)

#노드의 개수, 간선의 개수 입력 받기 / int 형으로 입력 받은 것을 공백으로 구분한다 
n, m = map(int,input().split())
#시작 노드 번호 입력 받기 = 시작점, 시작 노드를 입력받기 
start = int(input())
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만든다 /리스트 안에 리스트
graph = [[] for i in range (n+1)]
#방문한 기록이 있는지 확인하는 리스트 
visited = [False] * (n+1)
#최단 거리 테이블을 모두 무한으로 초기화를 한다 
distance = [INF] * (n+1)

#모든 간선 정보에 대해서 입력을 받는다 
for _ in range(m):
    a,b,c = map(int,input().split())
    #a 노드에서 b 노드로 가는데 발생하는 비용, 가중치 c 
    graph[a].append((b,c))

# 방문하지 않은 노드 들 중에서, 가장 거리가 짧은 노드를 반환한다 
def get_smallest_node():
    min_value = INF
    #최단 거리를 가진 노드를 가리키는 인덱스 
    min_index = 0 
    for i in range (1, n+1):
        #만약, 방문하지 않은 노드 들 중에서 min_value 보다 작은 거리 가 있다면,
        #최소 거리르 업데이트 해야한다 
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            min_index = i
    #최단 거리를 가리키는 노드 인덱스를 반환한다 
    return min_index 

def dijkstra(start):
    # 시작 노드의 경우 자기 자신에 대한 거리를 표시하는 것이므로 0으로 표기한다 
    distance[start] = 0 
    visited[start] = True 
    for j in graph[start]:
        distance[j[0]] = j[1]

    #시작 노드를 제외한 전체 n-1개의 노드에 대해서 거리를 계산 하는 과정을 반복한다 
    for i in range(n-1):
        # 현재 노드에 대해서는 방문 처리를 한다 
        now_node = get_smallest_node()
        visited[now_node] = True 
        #현재 노드와 연결된 다른 노드들의 거리를 확인한다 
        for j in graph[now_node]:
            #현재 노드를 거쳐서 다른 노드로 갈 때의 비용 
            cost = distance[now_node] + j[1]
            #현재 노드를 거쳐서 다른 노드로 갈때의 비용이 더 작을 경우 
            if cost < distance[j[0]]:
                #현재의 비용으로 업데이트 해준다 
                distance[j[0]] = cost


#다익스트라 알고리즘 수행 
dijkstra(start)

#모든 노드로 가기 위한 최단 거리를 출력 
for i in range(1,n+1):
    #노드간에 연결되어 있지 않을 경우 무한으로 출력한다 
    if distance[i] == INF:
        print("INFINITY")

    else:
        print(distance[i])
