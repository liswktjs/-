mygraph = {
    'vetices': ['A','B','C','D','E','F','G'],
    'edge' : [
        (7,'A','B'),
        (5,'A','D'),
        (7,'B','A'),
        (7,'B','E'),
        (8,'B','C'),
        (9,'B','D'),
        (5,'C','E'),
        (8,'C','B'),
        (5,'D','A'),
        (6,'D','F'),
        (7,'D','E'),
        (9,'D','B'),
        (7,'E','B'),
        (5,'E','C'),
        (7,'E','D'),
        (8,'E','F'),
        (9,'E','G'),
        (6,'F','D'),
        (8,'F','E'),
        (11,'F','G'),
        (9,'G','E'),
        (11,'G','F')
    ]
}

parent = dict()
rank = dict()

def find(node):
    #path compression 기법
    if parent[node] != node:
        #해당 노드가 부모노드를 가지고 있다는 의미 
        parent[node] = find(parent[node])
        #재귀호출로 최종적으로 부모 노드를 소환하게 된다 
    return parent[node]

def union(node_v,node_u):
    root1 = find(node_v)
    root2 = find(node_u)
    #각각의 노드에 대한 부모노드를 알아낸다

    if rank[root1] > rank[root2]:
        parent[root2] = root1
        #rank가 더 높은쪽으로(높이가 더 높은쪽으로) 그래프를 합쳐준다
    else:
        parent[root1] = root2

        if rank[root1] == rank[root2]:
            rank[root2] += 1 
        #연결 되었으므로 rank를 하나 더 올려준다 

def make_set(node):
#파라미터로 리스트의 원소 이름을 받는다 
    parent[node] = node
    #현재 자기 자신 밖에 없는 상태이기 때문에 부모노드는 자기 자신을 가리킨다 
    rank[node] = 0
    #높이는 현재 없는 상태이므로 


def kruskal(graph):
    mst = list()
    #탐색결과(=간선정보)를 return할 리스트를 만든다 
    # 1. 초기화
    for node in graph['vetices']:
    #각 노드별로 부분집합을 만드는 초기화 
        make_set(node)
        #초기화 하는 함수
    # 2. weight 기준으로 정렬
    edges = graph['edge']
    edges.sort()
    #가중치를 기준으로 정렬을 한다 

    # 3. 사이클이 없는 간선연결 
    for edge in edges:
    #가중치가 낮은 것 부터 꺼내기 시작한다 
        weight, node_v, node_u = edge
        #weight는 가중치, node_v는 목적지, node_u는 도착지
        if find(node_v) != find(node_u):
            #각자의 노드의 부모 노드가 같은지 검사한다 
            #순환으로 연결되지 않도록 검사하는 것 
            union(node_v, node_u)
            #부모노드가 같지 않으면 연결 될 수 있다
            mst.append(edge)
            #최소신장트리의 한 간선이 될 수 있다 

    return mst

print(kruskal(mygraph))