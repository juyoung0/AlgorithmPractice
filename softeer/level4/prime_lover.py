import sys
from collections import deque
import math

N, M = map(int, sys.stdin.readline().split())
levels = [[1000000001 for _ in range(N)] for _ in range(N)]
adjs = [[] for _ in range(N)]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for _ in range(M):
    a, b, l = map(int, sys.stdin.readline().split())
    levels[a-1][b-1] = min(l, levels[a-1][b-1])
    levels[b-1][a-1] = min(l, levels[b-1][a-1])
    adjs[a-1].append(b-1)
    adjs[b-1].append(a-1)

gyms = deque()
gyms.append(0)
levels[0][0] = 0
while gyms:
    gym = gyms.popleft()
    for adj in adjs[gym]:
        new_level = max(levels[gym][adj], levels[gym][gym])
        if  levels[adj][adj] > new_level:
            levels[adj][adj] = new_level
            gyms.append(adj)

n = levels[N-1][N-1] + 1
while not is_prime(n):
    n += 1
print(n)