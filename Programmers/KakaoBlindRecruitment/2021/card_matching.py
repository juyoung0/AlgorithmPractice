# 2100907: 순열조합으로 모든 카드 순서대로 보도록 했는데 정답율이 더 낮아짐...^^;

import itertools
from collections import deque
from collections import defaultdict

N = 4
board = [[]]
visited = [[200 for _ in range(N)] for _ in range(N)]
dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]
shape = defaultdict(list)
dist = {}

def ctrl(r, c, direction):
    if direction == 0: #'right'
        while c < N:
            c += 1
            if c != N and board[r][c] != 0:
                return (r, c)
        return (r, N-1)
    elif direction == 1: #'top':
        while r >= 0:
            r -= 1
            if r != -1 and board[r][c] != 0:
                return (r, c)
        return (0, c)
    elif direction == 2: #'left':
        while c >= 0:
            c -= 1
            if c != -1 and board[r][c] != 0:
                return (r, c)
        return (r, 0)
    elif direction == 3: #'down':
        while r < N:
            r += 1
            if r != N and board[r][c] != 0:
                return (r, c)
        return (N-1, c)
    return

def find_closer(r, c):
    # bfs 를 통해 제일 가까이에 있는 그림카드를 찾는다
    que = deque()
    que.append((r, c))
    candi = []
    while que:
        cur = que.popleft()
        for d in dir:
            next_r = cur[0] + d[0]
            next_c = cur[1] + d[1]
            if 0 <= next_r < N and 0 <= next_c < N:
                if board[next_r][next_c] != 0:
                    candi.append((next_r, next_c))
                que.append((next_r, next_c))

        if len(candi) != 0:
            break
    dist_temp = 100
    closer = None
    for c in candi:
        if dist[board[c[0]][c[1]]] < dist_temp:
            dist_temp = dist[board[c[0]][c[1]]]
            closer = c

    return closer

def find_way(r, c, g_r, g_c):
    global visited

    if r == g_r and c == g_c:
        return 0

    #print("visited ", r, c, step)
    for i in range(4):
        # ctrl 썼을 때
        ctrl_move = ctrl(r, c, i)
        if ctrl_move:
            n_r, n_c = ctrl_move[0], ctrl_move[1]
            if n_r == g_r and n_c == g_c:
                visited[g_r][g_c] = min(visited[g_r][g_c], visited[r][c])
                return
            if visited[n_r][n_c] > visited[r][c] + 1:
                visited[n_r][n_c] = visited[r][c] + 1
                find_way(n_r, n_c, g_r, g_c)

        # 한 칸 이동했을 때
        n_r, n_c = r + dir[i][0], c + dir[i][1]
        if 0 <= n_r < N and 0 <= n_c < N:
            if n_r == g_r and n_c == g_c:
                visited[g_r][g_c] = min(visited[g_r][g_c], visited[r][c] )
                return
            if visited[n_r][n_c] > visited[r][c] + 1:
                visited[n_r][n_c] = visited[r][c] + 1
                find_way(n_r, n_c, g_r, g_c)

    return

def solution(_board, r, c):
    global board, visited
    board = _board
    answer = 1000
    card_cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                card_cnt += 1
                shape[board[i][j]].append((i, j))

    # 어느 카드쌍을 먼저 지울지 고려할 때 활용
    for s in shape.keys():
        dist[s] = abs(shape[s][0][0]-shape[s][1][0]) + abs(shape[s][0][1]-shape[s][1][1])

    # 어떤 그림부터 뒤집을지 순열 만들기 (각 카드 두 쌍도 순서를 다르게 넣는다)
    # - 붙은 건 두번째 카드를 의미한다
    all_key = []
    for key in shape.keys():
        all_key.append(key)
        all_key.append(-key)
    card_order = itertools.permutations(all_key)

    for order in card_order:
        open = None
        step = 0
        cnt = card_cnt
        for card in order:
            #while cnt > 0:
            # 현재 위치에서 뒤집을 카드로 가는 거리 구하기
            if card < 0:
                card = abs(card)
                next_r, next_c = shape[card][1][0], shape[card][1][1]
            else:
                next_r, next_c = shape[card][0][0], shape[card][0][1]

            visited = [[200 for _ in range(N)] for _ in range(N)]
            visited[r][c] = 1
            find_way(r, c, next_r, next_c)
            step += visited[next_r][next_c]
            step += 1 # 카드 오픈

            if open == None:
                open = card
            elif open == card:
                # 짝이 맞는 카드 찾음
                if open == card:
                    board[r][c] = 0
                    board[next_r][next_c] = 0
                    cnt -= 2
                    #print("find : ", (r, c), (next_r, next_c), visited[r][c])
                open = None
            r, c = next_r, next_c
        if cnt == 0:
            if answer > step:
                #answer_list = order
                answer = step

    return step

print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0), 14)
print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1), 16)