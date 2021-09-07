# 2100907: 순열조합으로 모든 카드 순서대로 보도록 변경. 공간 탐색하는 부분 다익스트라로 변경
# 삽질 결과 느낀 점 1. 전역변수 사용 시에는 TC 여러개 돌릴 때 주의 하라. (프로그래머스 답과 달라서 오해할 수 있다)
# 느낀 점 2. 경로 탐색 등에서 map 을 재활용 할 때 초기값으로 셋팅하는 걸 주의하라
# 얕은 복사가 되면, 이미 기존 값이 다 날라가 버려서 다음 번 경로 계산시 틀린 값이 나온다
# copy 라이브러리의 deapcopy() 를 활용하라 => 시간 초과 날 수도 있으니 대안을 생각하라
# permutation 때문에 시간초과가 나는 것으로 보임 => 개선 필요!

import itertools
from collections import deque
from collections import defaultdict
import copy

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

def find_way(_r, _c):
    global visited
    pq = deque()
    pq.append((_r, _c))
    visited[_r][_c] = 0

    while len(pq) != 0:
        r, c = pq[0][0], pq[0][1]
        pq.popleft()

        for i in range(4):
            # ctrl 썼을 때 갈 수 있는 길
            ctrl_move = ctrl(r, c, i)
            if ctrl_move:
                n_r, n_c = ctrl_move[0], ctrl_move[1]
                # 한 칸 갈수있는 거리면 넣지 않는다 (아래에서 넣을 것이기 때문)
                if n_r - r != 1 and n_c - c != 1:
                    if visited[n_r][n_c] > visited[r][c] + 1:
                        pq.append((n_r, n_c))
                        visited[n_r][n_c] = visited[r][c] + 1

            # 한 칸 이동했을 때로 갈 수 있는 길
            n_r, n_c = r + dir[i][0], c + dir[i][1]
            if 0 <= n_r < N and 0 <= n_c < N:
                if visited[n_r][n_c] > visited[r][c] + 1:
                    pq.append((n_r, n_c))
                    visited[n_r][n_c] = visited[r][c] + 1
    return

def solution(_board, _r, _c):
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
        r, c = _r, _c
        # 초기화 된 보드 새로 셋팅하기
        for key in shape.keys():
            for i in shape[key]:
                board[i[0]][i[1]] = key
        #board = copy.deepcopy(_board)
        for card in order:
            # 현재 위치에서 뒤집을 카드로 가는 거리 구하기
            if card < 0:
                card = abs(card)
                next_r, next_c = shape[card][1][0], shape[card][1][1]
            else:
                next_r, next_c = shape[card][0][0], shape[card][0][1]

            # 짝이 안 맞을 경우 다른 순열로 넘어감
            if open != None and open != card:
                break

            visited = [[200 for _ in range(N)] for _ in range(N)]
            if r != next_r or c != next_c:
                find_way(r, c)
                step += visited[next_r][next_c]

            # 처음 뒤집는 카드
            if open == None:
                open = card
                step += 1  # 카드 오픈
            elif open == card:
                board[r][c] = 0
                board[next_r][next_c] = 0
                open = None
                step += 1  # 카드 오픈
                cnt -= 2

            r, c = next_r, next_c

        if cnt == 0:
            if answer > step:
                answer_list = order
                answer = min(answer, step)

    return answer

#print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0), 14)
print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1), 16)
