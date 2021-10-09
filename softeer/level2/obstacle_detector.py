import sys
from collections import deque

if __name__ == "__main__":
    n = int(input())
    road = ([list(map(int, input())) for _ in range(n)])
    visited = [[0 for _ in range(n)] for _ in range(n)]
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    group_id = 0
    answer = []
    pq = deque()

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and road[i][j] == 1:
                pq.clear()
                pq.append((i, j))
                group_id += 1
                while pq:
                    curr = pq.popleft()
                    visited[curr[0]][curr[1]] = group_id
                    for dir in dirs:
                        next_i, next_j = curr[0] + dir[0], curr[1] + dir[1]
                        if (0 <= next_i < n and 0 <= next_j < n) and visited[next_i][next_j] == 0 and road[next_i][
                            next_j] == 1:
                            pq.append((next_i, next_j))
                            visited[next_i][next_j] = group_id
                answer.append(sum(v.count(group_id) for v in visited))

    answer.sort()
    print(len(answer))
    for a in answer:
        print(a)