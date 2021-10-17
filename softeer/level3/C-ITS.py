import sys
from collections import deque

dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 0:오른쪽, 1:아래, 2:왼쪽, 3:위
# (오는 방향, 가는 방향들)
signals = [(2, [0, 1, 3]), (1, [0, 2, 3]), (0, [1, 2, 3]), (3, [0, 1, 2]),
            (2, [0, 3]), (1, [2, 3]), (0, [1, 2]), (3, [0, 1]),
            (2, [0, 1]), (1, [0, 3]), (0, [2, 3]), (3, [1, 2])]
N, T = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N*N)]
time_map = [[0 for _ in range(N)] for _ in range(N)]
time = 0
visited = []
to_visit = deque()

# (오는 방향, 가는 목적지)
start = (1, (0, 0))
to_visit.append(start)
while to_visit:
    curr = to_visit.popleft()

    # T시간을 넘어가면 종료한다
    time = time_map[curr[1][0]][curr[1][1]]
    if time > T:
        break

    if curr[1] not in visited:
        visited.append(curr[1])

    # 현재 시간 이 교차로에 켜져있는 신호를 가져온다
    num = curr[1][0] * N + curr[1][1]
    signal = signals[data[num][time%4] - 1]

    # 내가 오는 방향에 해당하는 신호여야지만 갈 수 있다
    if signal[0] == curr[0]:
        # 각 방향으로 갈 수 있다면 to_visit에 넣어준다
        for d in signal[1]:
            next_i, next_j = curr[1][0] + dirs[d][0], curr[1][1] + dirs[d][1]
            if 0 <= next_i < N and 0 <= next_j < N:
                # 지금 들어가는 방향 = 다음 위치에서 들어오는 방향이므로 180도 회전시켜서 넣어줘야함
                to_visit.append(((d + 2)%4, (next_i, next_j)))
                time_map[next_i][next_j] = time_map[curr[1][0]][curr[1][1]] + 1

print(len(visited))