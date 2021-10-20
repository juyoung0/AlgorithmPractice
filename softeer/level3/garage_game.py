import sys
from collections import deque

# 인풋 받기
n = int(sys.stdin.readline())
waits = []
garage = []
wait_idx = [2*n-1 for _ in range(n)]
for _ in range(2*n):
    waits.append(list(map(int, sys.stdin.readline().split())))
for _ in range(n):
    garage.append(list(map(int, sys.stdin.readline().split())))

# 빈칸을 새로 채우는 함수
def fill_garage(_garage, removed_num):
    global wait_idx, n
    for j in range(n):
        for i in range(removed_num[j]):
            print(i, j, removed_num[j])
            print(waits[wait_idx[j]])
            print()
            _garage[removed_num[j]-i-1][j] = waits[wait_idx[j]][j]
            wait_idx[j] -= 1
    return _garage

# 선택된 그룹을 지우는 함수
def remove_cars(_garage, group):
    global n
    min_x, min_y, max_x, max_y, score = n, n, -1, -1, 0
    removed_num = [0 for _ in range(n)]
    for g in group:
        min_x = min(min_x, g[0])
        max_x = max(max_x, g[0])
        min_y = min(min_y, g[1])
        max_y = max(max_y, g[1])
        removed_num[g[1]] += 1
        score += _garage[g[0]][g[1]]
        _garage[g[0]][g[1]] = -1

    # 현재 있는 차들을 내려서 지운 칸 채우기
    for j in range(n):
        for i in range(n-2, -1, -1):
            k = i
            if _garage[k][j] != -1:
                while k+1 < n and _garage[k+1][j] == -1:
                    _garage[k+1][j] = _garage[k][j]
                    _garage[k][j] = -1
                    k += 1

    score += (max_x - min_x + 1) * (max_y - min_y + 1)
    return fill_garage(_garage, removed_num), score

# 다음에 누를 수 있는 버튼 그룹 찾기 (bfs)
def find_groups(_garage):
    global n
    visited = [[0 for _ in range(n)] for _ in range(n)]
    groups = []

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1:
                continue

# 매 turn 마다 지울수 있는 group 찾아서 지우고 점수 비교하기
def dfs(_garage, turn, score):
    if turn > 3:
        return score
    _score = score
    groups = find_groups(_garage)
    for group in groups:
        _new_garage, _new_score = remove_cars(_garage, group)
        _score = max(_score, dfs(_new_garage, turn+1, score+_new_score))
    return _score

print(def(garage, 1, 0))