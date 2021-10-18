# 1. color 별로 dfs 를 돌리는 방법
# 정확도는 맞으나 시간초과가 남
# 2. x축 기준으로 sort하고 범위를 넓혀가며 검사하는 방법
# 전체 탐색을 하는 경우가 1번보다 적음 (앞에서 최저값 찾은 경우, 그 값보다 커지는 케이스에서 break 가능)

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
points = []
for _ in range(N):
    x, y, k = map(int, sys.stdin.readline().split())
    points.append((x, y, k))
points.sort(key=lambda p: p[0])
result = 4000001

# x축 정렬한 기준 왼쪽부터 차례로 width 넓혀나간다
for i in range(N):
    for j in range(i, N):
        colors = [0 for _ in range(K)]
        color_cnt = 0
        width = points[j][0] - points[i][0]
        # min_y, max_y = min(points[j][0], points[j][1]), max(points[j][0], points[j][1])
        subs = sorted(points[i:j + 1], key=lambda x: x[1])
        start, end = 0, -1

        # i와 j 점 사이에 있는 점들 체크하기
        # start - end 로 범위 나눠서 비교해보기
        while end < len(subs):
            if color_cnt < K:
                end += 1
                if end == len(subs):
                    break
                colors[subs[end][2] - 1] += 1
                if colors[subs[end][2] - 1] == 1:
                    color_cnt += 1

            if color_cnt == K:
                result = min(result, width * (subs[end][1] - subs[start][1]))
                colors[subs[start][2] - 1] -= 1
                if colors[subs[start][2] - 1] == 0:
                    color_cnt -= 1
                start += 1

print(result)

# 1번 방법
# import sys
# from collections import deque
#
# def area(points):
#     max_x, max_y, min_x, min_y = -1000, -1000, 1000, 1000
#     for point in points:
#         max_x, max_y = max(max_x, point[0]), max(max_y, point[1])
#         min_x, min_y = min(min_x, point[0]), min(min_y, point[1])
#     return (max_x - min_x) * (max_y - min_y)
#
# result = 4000001
#
# def dfs(points, k):
#     global K, result
#     if k == K:
#         return area(points)
#
#     #이미 구해놓은 넓이보다 커지면 바로 종료
#     if area(points) >= result:
#         return 4000001
#
#     _result = 4000001
#     for p in colors[k]:
#         points.append(p)
#         _result = min(_result, dfs(points, k+1))
#         points.pop()
#     return _result
#
# N, K = map(int, sys.stdin.readline().split())
# colors = [[] for _ in range(K)]
# for _ in range(N):
#     x, y, k = map(int, sys.stdin.readline().split())
#     colors[k-1].append((x, y))
#
# points = deque()
#
# # 색깔별로 하나씩 추출해서 넓이 구해보기
# for p in colors[0]:
#     points.append(p)
#     result = min(result, dfs(points, 1))
#     points.pop()
#
# print(result)