import heapq

#가중치와 함께 연결되어 있는 그래프 예시 
graph ={
    'A':{'B':8, 'C':1, 'D':2},
    'B':{},
    'C':{'B':5, 'D':2},
    'D':{'E':3, 'F':5},
    'E':{'F':1},
    'F':{'A':5}
}

def dijkstra(graph, start_node):

    # start node와 연결되는 노드들을 알아내기 전에 
    # start node와의 거리를 모두 inf로(=무한대) 설정한다
    distances = {node: float('inf') for node in graph}
    # 자기자신을 가리키는 것이므로 start_node의 거리는 0이 된다
    distances[start_node] = 0
    # 우선 순위를 저장해 놓기 위한 queue를 생성한다 
    queue = []
    # heap queue에 start_node에 대한 정보를 넣어준다 
    heapq.heappush(queue, [distances[start_node],start_node])
   
    # = > 초기화 설정 완료
    
    #queue에 원소가 있는 동안 while문이 반복되게 된다 
    while queue:
        # heapqueue에서 현재의 노드와 현재의 노드가 다른 노드를 가기 위한 거리 가중치 값을 가지고 온다
        current_distance, current_node = heapq.heappop(queue)

        #찾아낸 거리가 원래 있었던 거리보다 클 경우 업데이트를 해줄 필요가 없다 
        if distances[current_node] < current_distance:
            continue

        #adjacent = 인접한 노드의 이름, weight = 그 노드로 가는데 걸리는 가중치 값 
        for adjacent, weight in graph[current_node].items():
            #weight와 node간의 거리를 합한 것 
            distance = current_distance + weight
            #최단 거리를 발견했다는 의미 
            if distance < distances[adjacent]:
                #최단 거리를 발견했으므로 발견된 거리로 업데이트를 해준다
                distances[adjacent] = distance 
                #heap에 해당 내용을 push한다 
                heapq.heappush(queue,[distance,adjacent])
    
    return distances

print(dijkstra(graph, 'A'))


