#위상정렬 구현 

from collections import deque

v, e = map(int,input().split())
#모든 노드에 대해서 진입차수 0으로 초기화
indegree = [0] * (v+1)
#각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v+1)]

#방향 그래프의 간선에 대한 정보 입력받기 

for _ in range(e):
    a, b = map(int,input().split())
    #노드 a에서 b로 이동가능
    graph[a].append(b)
    #b에 대한 진입차수 1 증가
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        #진입차수가 0 인 노드를 삽입
        if indegree[i] == 0:
            q.append(i)

    #q가 빌때까지 반복
    while q:
        now = q.popleft()
        result.append(now)
        #해당원소와 연결된 노드들의 진입차수 1씩 빼기
        for i in graph[now]:
            indegree[i] -= 1
            #진입차수가 0인 노드를 q에 삽입
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=" ")

topology_sort()