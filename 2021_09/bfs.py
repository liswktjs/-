# 너비 우선 탐색 그래프
# 그래프 예시
'''
             A
        B         C
    D     E     F    G
H              I 
방문순서 : A -> B -> C -> D -> E ->F ->G ->H -> I
'''

#queeu 자료형을 사용해야 하므로 import (list를 활용하는 방법도 존재한다)
from collections import deque
graph = dict()
#인접리스트 방식 
graph['A'] = ['B', 'C']
graph['B'] = ['A','D', 'E']
graph['C'] = ['A','F', 'G']
graph['D'] = ['B', 'H']
graph['E'] = ['B']
graph['F'] = ['C', 'I']
graph['G'] = ['C']
graph['H'] = ['D']
graph['I'] = ['F']

def BFS (graph, start_node) :
    #방문해야할 곳들 
    need_queue = deque()
    #방문한 곳들 
    visitied = list()

    #처음시작 노드를 넣어준다
    need_queue.append(start_node)

    while need_queue:
        #맨 앞에 위치한 노드를 꺼낸다
        node = need_queue.popleft()
        #만약 해당 노드가 아직 방문하지 않았다면
        if node not in visitied:
            #방문처리를 해준다
            visitied.append(node)
            #방문처리를 해준 노드의 인접 노드를 방문해야할 노드로 추가 해준다
            need_queue.extend(graph[node])

    return visitied

print(BFS(graph, 'A'))