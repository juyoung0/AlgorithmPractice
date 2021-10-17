import sys
from collections import deque

H, W = map(int, sys.stdin.readline().split())
data = [list(sys.stdin.readline().strip()) for _ in range(H)]
starts = deque()
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
arrows = [">", "v", "<", "^"]
left_d = [(0, 3), (1, 0), (2, 1), (3, 2)]
right_d = [(3, 0), (0, 1), (1, 2), (2, 3)]
route_len, answer = H*W, []

# 시작점 후보리스트를 만든다. 인접한 #가 1개밖에 없을 경우 출발지, 또는 도착지이다
for i in range(H):
    for j in range(W):
        if '#' == data[i][j]:
            cnt = 0
            for dir in dirs:
                next_i, next_j = i + dir[0], j + dir[1]
                if 0 <= next_i < H and 0 <= next_j < W and data[next_i][next_j] == '#':
                    cnt += 1
            if cnt == 1:
                starts.append((i, j))

# 각 시작점으로 부터 dfs 탐색을 하여 숫자를 구한다
def dfs(i, j):
    visited = []
    to_visit = deque()
    to_visit.append((i, j))
    route = []
    way = -1
    while to_visit:
        curr = to_visit.popleft()
        visited.append(curr)
        for d, dir in enumerate(dirs):
            next_i, next_j = curr[0] + dir[0], curr[1] + dir[1]
            if 0 <= next_i < H and 0 <= next_j < W and data[next_i][next_j] == '#' and (next_i, next_j) not in visited:
                # 최초 방향 넣어주기
                if len(route) == 0:
                    route.append(arrows[d])
                    way = d
                else:
                    # 방향이 바뀔 경우 회전방향 구해주기
                    if (way, d) in left_d:
                        route.append('L')
                    elif (way, d) in right_d:
                        route.append('R')
                    way = d

                # 두 칸을 진행하므로 지나가는 경로를 visited에 넣어주어야 한다
                # 두 칸 전진한 후의 위치를 to_visit에 넣어준다
                route.append('A')
                visited.append((next_i, next_j))
                to_visit.append((curr[0] + dir[0]*2, curr[1] + dir[1]*2))
                break
    return route

for start in starts:
    route = dfs(start[0], start[1])
    if len(route) < route_len:
        start_point = start
        answer = route
        route_len = len(route)

print(start_point[0]+1, start_point[1]+1)
print(answer[0])
print("".join(answer[1:]))