import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
data = [[] for i in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
w, h, r = (0, 0), (0, 0), (0, 0)
pq = deque()
rains = deque()
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def spand_rain():
    global rains
    _rains = deque()
    while rains:
        curr = rains.popleft()

        # "."인 구역으로 비확장시키기
        for dir in dirs:
            next_r, next_c = curr[0] + dir[0], curr[1] + dir[1]
            if 0 <= next_r < R and 0 <= next_c < C and visited[next_r][next_c] == 0 and data[next_r][next_c] == ".":
                data[next_r][next_c] = "*"
                _rains.append((next_r, next_c))

    rains = _rains

for i in range(R):
    data[i] = list(sys.stdin.readline())
    for j in range(C):
        if data[i][j] == 'H':
            h = (i, j)
        elif data[i][j] == '*':
            r = (i, j)
            rains.append(r)
        elif data[i][j] == 'W':
            w = (i, j)

pq.append(w)
visited[w[0]][w[1]] = 1
time = 0
while pq:
    curr = pq.popleft()

    # 시간이 지났다면 소나기의 범위를 확장시킨다
    if visited[curr[0]][curr[1]] != time:
        spand_rain()
        time = visited[curr[0]][curr[1]]
    if curr == h:
        break
    for dir in dirs:
        next_r, next_c = curr[0] + dir[0], curr[1] + dir[1]
        # 갈 수 있는 길이면 visited에 시간을 기록하고 pq에 추가한다
        if 0 <= next_r < R and 0 <= next_c < C and visited[next_r][next_c] == 0 and (data[next_r][next_c] == "." or data[next_r][next_c] == "H"):
            visited[next_r][next_c] = visited[curr[0]][curr[1]] + 1
            pq.append((next_r, next_c))

if visited[h[0]][h[1]] == 0:
    print("FAIL")
else:
    print(visited[h[0]][h[1]] - 1)