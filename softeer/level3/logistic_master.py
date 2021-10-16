import sys

n, m, k = map(int, input().split())
rail = list(map(int, input().split()))
rail.sort()
rail_sort = []
for i in range(n//2):
    if n % 2 == 0:
        rail_sort.append(rail[i + n//2])
    else:
        rail_sort.append(rail[i + n//2 + 1])
    rail_sort.append(i)

if n % 2 == 1:
    rail_sort.append(rail[n//2])

print(rail_sort)
