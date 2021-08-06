p, m = map(int, input().split())
m_list = list(map(int, input().split()))

max_num = 0

for i in m_list:
    if i % 2 == 0:
        max_num += int(i / 2)
    else:
        max_num += int(i / 2) + 1

if p <= max_num:
    print("YES")
else:
    print("NO")