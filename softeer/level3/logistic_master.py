import sys
from itertools import permutations

n, M, k = map(int, input().split())
rail = list(map(int, input().split()))
rails = permutations(rail, len(rail))

answer = 50*50
for r in rails:
    i, m, total = 0, 0, 0
    for _ in range(k):
        while m + r[i] <= M:
            m += r[i]
            i += 1
            i %= n
        total += m
        m = 0
        if total >= answer:
            break
    answer = min(total, answer)

print(answer)