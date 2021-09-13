graph = {
    'nodes': ['A','B','C','D','E','F','G'],
    'edges': [ #weight, 시작노드, 끝노드
        (7,'A','B'),
        (5,'A','D'),
        (7,'B','A'),
        (8, 'B','C'),
        (9,'B','D'),
        (7,'B','E'),
        (8,'C','B'),
        (5,'C','E'),
        (5,'D','A'),
        (9,'D','B'),
        (7,'D','E'),
        (6,'D','F'),
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

def make_set(node):
    parent[node] = node
    rank[node] = 0

def find(node):
    #path compression기법 사용 
    if parent[node] != node:
        parent[node] = find(parent[node])
    #루트노드를 return 한다 
    return parent[node]

def union(node_v, node_u):
    #union-by-rank기법 사용 
    root1 = find(node_v)
    root2 = find(node_u)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2

        if rank[root1] == rank[root2]:
            rank[root2] += 1

def kruskal(graph):
    #cycle이 없다면 간선정보를 mst에 저장해서 return한다
    mst = list()

    #각 노드별로 부분집합 만들기(초기화)
    for node in graph['nodes']:
        make_set(node)

    #sorting하기 / weight가 낮은 순서대로
    edges = graph['edges']
    edges.sort()

    #노드들이 중복되는지 확인
    for edge in edges:
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(edge)

    
    return mst

print(kruskal(graph)) 