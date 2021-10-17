import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
ice = sum(sum(a) for a in data)
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
time = 0


# 공기가 외부 공기인지, 내부 공기인지 판단하기 위한 용도
# (0, 0)으로 부터 이어지는 공기인지 아닌지 판단한다
# 2 : 외부 공기, 0: 내부 공기
def change_air(i, j):
    airs = deque()
    airs.append((i, j))
    while airs:
        curr = airs.popleft()
        for dir in dirs:
            next_n, next_m = curr[0] + dir[0], curr[1] + dir[1]
            if 0 <= next_n < N and 0 <= next_m < M and data[next_n][next_m] == 0:
                data[next_n][next_m] = 2
                airs.append((next_n, next_m))


change_air(0, 0)

while ice > 0:
    melted = []
    for i in range(N):
        for j in range(M):
            # 다음에 녹을 얼음인지 아닌지 판단
            if data[i][j] == 1:
                air = 0
                for dir in dirs:
                    if data[i + dir[0]][j + dir[1]] == 2:
                        air += 1
                if air >= 2:
                    ice -= 1
                    melted.append((i, j))

    # 녹은 부분은 0으로 만들어주면서 내부공기 체크하기
    # print(melted, ice)
    for m in melted:
        data[m[0]][m[1]] = 2
        change_air(m[0], m[1])
    time += 1

print(time)