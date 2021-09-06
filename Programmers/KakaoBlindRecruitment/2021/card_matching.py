# 2100906: 2시간 했으나 못품

from collections import deque
from collections import defaultdict

N = 4
board = [[]]
visited = [[0 for _ in range(N)] for _ in range(N)]
dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]
shape = defaultdict(list)

def ctrl(r, c, direction):
    if direction == 0: #'right'
        while c < N:
            c += 1
            if c == N: return None
            if board[r][c] != 0:
                break
    elif direction == 1: #'top':
        while r >= 0:
            r -= 1
            if r == -1: return None
            if board[r][c] != 0:
                break
    elif direction == 2: #'left':
        while c >= 0:
            c -= 1
            if c == -1: return None
            if board[r][c] != 0:
                break
    elif direction == 3: #'down':
        while r < N:
            r += 1
            if r == N: return None
            if board[r][c] != 0:
                break

    return (r, c)

def find_closer(r, c):
    # bfs 를 통해 제일 가까이에 있는 그림카드를 찾는다
    que = deque()
    que.append((r, c))
    while que:
        cur = que.popleft()
        for d in dir:
            next_r = cur[0] + d[0]
            next_c = cur[1] + d[1]
            if 0 <= next_r < N and 0 <= next_c < N:
                if board[next_r][next_c] != 0:
                    return (next_r, next_c)
                que.append((next_r, next_c))

    return -1

def find_way(r, c, g_r, g_c, step):
    global visited

    visited[r][c] = 1
    #print("visited ", r, c, step)
    step1, step2 = 20, 20
    for i in range(4):
        # ctrl 썼을 때
        ctrl_move = ctrl(r, c, i)
        if ctrl_move:
            n_r, n_c = ctrl_move[0], ctrl_move[1]
            if n_r == g_r and n_c == g_c:
                return step
            if visited[n_r][n_c] == 0:
                #print("---", n_r, n_c, "---")
                step1 = find_way(n_r, n_c, g_r, g_c, step+1)
        # 한 칸 이동했을 때
        n_r, n_c = r + dir[i][0], c + dir[i][1]
        if 0 <= n_r < N and 0 <= n_c < N:
            if n_r == g_r and n_c == g_c:
                return step
            if visited[n_r][n_c] == 0:
                #print("---", n_r, n_c, "---")
                step2 = find_way(n_r, n_c, g_r, g_c, step+1)

    return min(step1, step2)

def solution(_board, r, c):
    global board, visited
    board = _board
    step = 0
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                cnt += 1
                shape[board[i][j]].append((i, j))

    while cnt > 0:
        #print("visited ", r, c)

        if board[r][c] == 0:
            next_r, next_c = find_closer(r, c)
            step += int(next_r != r) + int(next_c != c)
            r, c = next_r, next_c
            #print("visited ", r, c)

        if shape[board[r][c]][0][0] == r and shape[board[r][c]][0][1] == c:
            next_r, next_c = shape[board[r][c]][1][0], shape[board[r][c]][1][1]
        else:
            next_r, next_c = shape[board[r][c]][0][0], shape[board[r][c]][0][1]
        #print("=========", r, c, "===========")
        step += find_way(r, c, next_r, next_c, 0)
        visited = [[0 for _ in range(N)] for _ in range(N)]
        board[r][c] = 0
        board[next_r][next_c] = 0
        #print("remove ", r, c, next_r, next_c)
        cnt -= 2
        r, c = next_r, next_c

    return step

print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0), 14)
#print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1), 16)