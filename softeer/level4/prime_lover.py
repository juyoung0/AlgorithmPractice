# 런타임 에러와 시간초과를 해결한 문제
# 에라토스테네스의 체 보다는 소수판별 알고리즘이 빠른 문제
# N의 최대값은 10,000인데 2d-array를 만들다보니 정해진 메모리를 다 사용해서 런타임에러 발생
# levels 2d array를 min_level 1d array 하나와, adjs에 튜플을 넣는 방식으로 수정함
# 시간제한 초과가 발생한 부분은 gyms에 adj가 있는지 보고 넣는 부분이었는데
# list에서 item이 있는지 없는지 확인하는 부분이 시간초과 발생하였음

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
adjs = [[] for _ in range(N)]
min_level = [1000000001 for _ in range(N)]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for _ in range(M):
    a, b, l = map(int, sys.stdin.readline().split())
    adjs[a-1].append((b-1, l))
    adjs[b-1].append((a-1, l))

gyms = deque()
gyms.append(0)
min_level[0] = 0
while gyms:
    gym = gyms.popleft()
    for adj in adjs[gym]:
        if adj[0] == gym:
            continue
        new_level = max(adj[1], min_level[gym])
        if  min_level[adj[0]] > new_level:
            min_level[adj[0]] = new_level
            gyms.append(adj[0])

n = min_level[N-1] + 1
while not is_prime(n):
    n += 1
print(n)

#
# import sys
# from collections import deque
# import math
#
# N, M = map(int, sys.stdin.readline().split())
# levels = [[1000000001 for _ in range(N)] for _ in range(N)]
# adjs = [[] for _ in range(N)]
#
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True
#
# for _ in range(M):
#     a, b, l = map(int, sys.stdin.readline().split())
#     levels[a-1][b-1] = min(l, levels[a-1][b-1])
#     levels[b-1][a-1] = min(l, levels[b-1][a-1])
#     adjs[a-1].append(b-1)
#     adjs[b-1].append(a-1)
#
# gyms = deque()
# gyms.append(0)
# levels[0][0] = 0
# while gyms:
#     gym = gyms.popleft()
#     for adj in adjs[gym]:
#         new_level = max(levels[gym][adj], levels[gym][gym])
#         if levels[adj][adj] > new_level:
#             levels[adj][adj] = new_level
#             if adj not in gyms:
#               gyms.append(adj)
#
# n = levels[N-1][N-1] + 1
# while not is_prime(n):
#     n += 1
# print(n)