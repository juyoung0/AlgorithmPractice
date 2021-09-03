from collections import deque

def solution(n, edge):
    visited = [0] * (n + 1)
    edges = [[] for i in range(n + 1)]
    answer = 0

    for e in edge:
        edges[e[0]].append(e[1])
        edges[e[1]].append(e[0])

    prev = 1
    visited[0] = -1
    visited[1] = prev
    queue = deque(edges[1])
    temp = deque()

    #모든 노드를 방문할 때까지 순회
    while 0 in visited:
        prev += 1
        while len(queue) != 0:
            node = queue.popleft()
            if visited[node] == 0:
                visited[node] = prev
                temp.extend(edges[node])

        queue = temp
        temp = deque()

    answer = visited.count(prev)

    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 3)