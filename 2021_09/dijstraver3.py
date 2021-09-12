#리스트 형태가 사전에 정해져있을때에 

import heapq
def dijktra(graph, start):
    
    #출발점과 각 노드간의 최단거리를 저장할 리스트 생성
    #graph에 있는 a,b,c,d를 node를 통해서 순회하면서 distance에 INF로 초기화 기록 
    distances = {node:int(1e9) for node in graph}

    distances[start] = 0 
    queue = []

    #queue에 거리값과 노드 순서대로 리스트에 넣어준다
    heapq.heappush(queue, [distances[start], start]) #0, 'A'순서대로 들어갔다 

    while queue:
        current_distance, current_node = heapq.heappop(queue) #0,'A'방식으로 데이터가 추출된다

        if distances[current_node] < current_distance:
            continue

        #인접된 노드의 이름, 노드에 접근할때의 거리값 순서대로 추출이된다
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight 

            #만약 인접노드를 거쳐 목표 node까지 가는 weight이 기존의 route보다 작다면 
            #queue에 update를 해준다
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances

#사전형태
mygraph = {
    'A':{'B':8, 'C': 1, 'D': 2},
    'B': {},
    'C' : {'B':5, 'D':2},
    'D' : {'E':3, 'F': 5},
    'E' : {'F': 1},
    'F' : {'A': 5}
}

print(dijktra(mygraph, 'A'))