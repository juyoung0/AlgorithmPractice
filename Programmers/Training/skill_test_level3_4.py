# 섬 사이 다리 건설 (최소 비용 스패닝 트리)
# 크루스칼 알고리즘

# Kruskal Algorithm
import math

parent = dict()
rank = dict()


# vertice 초기화
def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0


# 해당 vertice의 최상위 정점을 찾는다
def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]


# 두 정점을 연결한다
def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1


def kruskal(vertices, edges):
    minimum_spanning_tree = []

    # 초기화
    for vertice in vertices:
        make_set(vertice)

    # 간선 연결 (사이클 없게)
    for edge in edges:
        vertice1, vertice2, weight = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.append(edge)

    return minimum_spanning_tree


def solution(n, costs):
    vertices = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])

    tree = kruskal(vertices, costs)

    answer = 0
    for t in tree:
        answer += t[2]
    return answer