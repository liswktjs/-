# 깊이 우선 탐색 그래프
# 그래프 예시 
#             A
#        B         C
#    D     E     F    G
#H              I 
#방문순서 :    A -> C -> G -> F -> I -> B->E -> D -> H

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

def DFS (graph, start_node):
    #방문여부 기록할 stack 
    need_stack = list()
    #방문 순서대로 기록할 list 
    visitied = list()
    need_stack.append(start_node)

    while need_stack:
        #스택에서 방문할 노드를 뽑는다
        node = need_stack.pop()

        #만약 stack에서 가지고 온 node가 방문하지 않았더라면
        if node not in visitied:
            #해당 노드를 방문처리한다 
            visitied.append(node);
            #해당 노드의 인접 노드를 방문해야 할 노드로 넣는다
            need_stack.extend(graph[node])

    return visitied

print(DFS(graph, 'A'))