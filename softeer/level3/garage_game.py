# 시간초과 남
# 1. 위에서 아래로 내려오는 테트리스 구조이므로 행,열이 아닌 열,행으로 저장함
# 2. 빈칸 채울떄 하나씩 이동하지 않고, 남아있는 차를 모아서 한번에 이동시킴
# 3. 뭘 더 해야 할까..?

import sys
from collections import deque
import copy

# 인풋 받기
n = int(sys.stdin.readline())
waits = [[0 for _ in range(2*n)] for _ in range(n)]
garage = [[0 for _ in range(n)] for _ in range(n)]
max_answer, min_answer = 0, 0
wait_idx = [2*n for _ in range(n)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for j in range(2*n):
    data = list(map(int, sys.stdin.readline().split()))
    for i in range(n):
        waits[i][j] = data[i]
for j in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    for i in range(n):
        garage[i][j] = data[i]

# 빈칸을 새로 채우는 함수
def fill_garage(_garage, removed_num, _wait_idx):
    global n
    for i in range(n):
        _garage[i][:removed_num[i]] = waits[i][_wait_idx[i]-removed_num[i]:_wait_idx[i]]
        _wait_idx[i] -= removed_num[i]

    return _garage, _wait_idx

# 선택된 그룹을 지우는 함수
def remove_cars(_garage, group, _wait_idx):
    global n
    min_x, min_y, max_x, max_y, score = n, n, -1, -1, 0
    removed_num = [0 for _ in range(n)]
    for g in group:
        min_x = min(min_x, g[0])
        max_x = max(max_x, g[0])
        min_y = min(min_y, g[1])
        max_y = max(max_y, g[1])
        removed_num[g[0]] += 1
        _garage[g[0]][g[1]] = -1

    # 현재 있는 차들을 내려서 지운 칸 채우기 (버전 1)
    # for j in range(n):
    #     for i in range(n-2, -1, -1):
    #         k = i
    #         if _garage[k][j] != -1:
    #             while k+1 < n and _garage[k+1][j] == -1:
    #                 _garage[k+1][j] = _garage[k][j]
    #                 _garage[k][j] = -1
    #                 k += 1

    # 현재 있는 차들을 내려서 지운 칸 채우기 (버전 2)
    _temp = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        idx = n-1
        for j in range(n-1, -1, -1):
            if _garage[i][j] != -1:
                _temp[i][idx] = _garage[i][j]
                idx -= 1

    score += len(group)
    score += (max_x - min_x + 1) * (max_y - min_y + 1)
    return fill_garage(_temp, removed_num, _wait_idx[:]), score

# 다음에 누를 수 있는 버튼 그룹 찾기 (bfs)
def find_groups(_garage):
    global n, dirs
    visited = [[0 for _ in range(n)] for _ in range(n)]
    _groups = []

    for j in range(n):
        for i in range(n):
            if visited[i][j] == 1:
                continue
            group = []
            group.append((i, j))
            pq = deque()
            pq.append((i, j))
            color = _garage[i][j]
            visited[i][j] = 1

            while pq:
                curr = pq.popleft()
                for dir in dirs:
                    next_x, next_y = curr[0] + dir[0], curr[1] + dir[1]

                    if 0<=next_x<n and 0<=next_y<n:
                        if visited[next_x][next_y] == 0 and _garage[next_x][next_y] == color:
                            group.append((next_x, next_y))
                            pq.append((next_x, next_y))
                            visited[next_x][next_y] = 1
            _groups.append(group)

    return _groups

# 매 turn 마다 지울수 있는 group 찾아서 지우고 점수 비교하기
def dfs(_garage, turn, score, _wait_idx):
    global max_answer, min_answer
    if turn > 3:
        min_answer = min(min_answer, score)
        max_answer = max(max_answer, score)
    else:
        groups = find_groups(_garage)
        for group in groups:
            (_new_garage, _new_wait_idx), _new_score = remove_cars(copy.deepcopy(_garage), group, _wait_idx[:])
            dfs(_new_garage, turn+1, score+_new_score, _new_wait_idx[:])

dfs(garage, 1, 0, wait_idx)
print(max_answer)
