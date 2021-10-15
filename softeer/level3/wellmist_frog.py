n, m = map(int, input().split())
weight = list(map(int, input().split()))
best = [1 for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    if weight[a-1] < weight[b-1]:
        best[a-1] = 0
    elif weight[a-1] > weight[b-1]:
        best[b-1] = 0
    else:
        best[a-1] = 0
        best[b-1] = 0

print(best.count(1))