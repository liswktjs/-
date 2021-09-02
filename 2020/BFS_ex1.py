def bfs(graph, start_node):
    #방문한 곳과, 방문해야할 곳들의 원소들을 가지는 리스트를 생성한다 
    visited = list()
    need_visit = list()

    #탐색을 시작해야할 노드는 방문을 해야하는 노드이므로 
    #방문해야하는 곳들의 원소들을 가지는 리스트에 원소를 붙인다 
    need_visit.append(start_node)

    #need_visit 리스트의 원소들이 존재하지 않을 때 까지 while문을 반복한다
    while need_visit:
        #need_visit list에서 맨 앞의 노드를 pop해서 가지고 온다 
        node = need_visit.pop(0)
        #만약 맨앞의 노드가 visited list에 속한 노드가 아니라면 
        #맨 앞의 노드가 방문해야할 노드이므로 방문을 한다 
        if node not in visited:
            #이제 앞의 노드는 방문한 것이 되므로 
            #visited_list에 노드를 붙여준다 
            visited.append(node)
            #need_vist에 방문해야할 노드를 업데이트 한다 
            #*extend는 리스트를 붙여야 할 때 사용하는 함수이다
            need_visit.extend(graph[node])

    #너비우선 탐색 순서대로 정렬된 visited list을 반환한다 
    return visited

graph = dict()
#각 노드와 인접한 노드를 묶어준다
graph['A'] = ['B','C']
graph['B'] = ['A','D','E']
graph['C'] = ['A','F']
graph['D'] = ['B','G']
graph['E'] = ['B','H']
graph['F'] = ['C','I']
graph['G'] = ['D']
graph['H'] = ['E']
graph['I'] = ['F']

print(bfs(graph,'A'))