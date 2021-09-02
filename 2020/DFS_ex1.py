def dfs(graph, start_node):
    #방문한 곳과, 방문해야할 곳들의 원소들을 가지는 리스트를 생성한다 
    visited = list()
    need_visit = list()
    
    #파라미터로 넘겨 받은 start_node 부터 탐색을 시작해야하므로,
    #need_visit리스트에 start_node를 붙인다 
    need_visit.append(start_node)

    #need_visit 리스트의 원소들이 존재하지 않을 때 까지 while 문을 반복한다
    while need_visit:
        #깊이 우선 탐색을 해야하기 때문에, need_visit 리스트의
        #맨 마지막 노드를 pop 해서 가지고 온다 
        #=마지막으로 삽입된 노드를 가지고 오는 것 (후입선출)
        node = need_visit.pop()
        #만약 pop한 node를 아직 방문하지 않았다면, 
        if node not in visited:
            #node를 visited리스트에 붙여 방문한 것으로 처리 해준다
            visited.append(node)
            #need_visit에 현재 해당하는 노드의 인접한 노드들을 
            #원소로 추가해준다 
            need_visit.extend(graph[node])

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

print(dfs(graph,'A'))