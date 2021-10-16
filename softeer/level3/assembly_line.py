# 시간초과나서 수정함

import sys

n = int(input())
time = [[0 for _ in range(n)] for _ in range(2)]

if n == 1:
    a, b = map(int, sys.stdin.readline().split())
    print(min(a, b))
else:
    a, b, prev_a_t, prev_b_t = map(int, sys.stdin.readline().split())
    time[0][0] = a
    time[1][0] = b

    for i in range(1, n-1):
        a, b, a_t, b_t = map(int, sys.stdin.readline().split())
        time[0][i] = min(time[0][i-1], time[1][i-1] + prev_b_t) + a
        time[1][i] = min(time[1][i-1], time[0][i-1] + prev_a_t) + b
        prev_a_t, prev_b_t = a_t, b_t

    a, b = map(int, sys.stdin.readline().split())
    time[0][n-1] = min(time[0][n-2], time[1][n-2] + prev_b_t) + a
    time[1][n-1] = min(time[1][n-2], time[0][n-2] + prev_a_t) + b

    print(min(time[0][n-1], time[1][n-1]))

# import sys
# n = int(input())
# work = [[] for _ in range(2)]
# move = [[] for _ in range(2)]
#
# def calc(w, i):
#     if i == 0:
#         return work[w][i]
#     else:
#         return min(calc(w, i-1), calc(abs(w-1), i-1) + move[abs(w-1)][i-1]) + work[w][i]
#
# for _ in range(n-1):
#     a, b, a_t, b_t = map(int, sys.stdin.readline().split())
#     work[0].append(a)
#     work[1].append(b)
#     move[0].append(a_t)
#     move[1].append(b_t)
# a, b = map(int, sys.stdin.readline().split())
# work[0].append(a)
# work[1].append(b)
#
# print(min(calc(0, n-1), calc(1, n-1)))