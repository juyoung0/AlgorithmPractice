# O(N^2) 로 풀었더니 시간초과나서 O(nlogN)으로 풀어야
import sys

# 시간초과 코드
# if __name__ == "__main__":
#     n = int(input())
#     stone = list(map(int, input().split()))
#     step_l = [1 for _ in range(n)]
#     step_r = [1 for _ in range(n)]
#     for i in range(1, n):
#         for j in range(i):
#             if stone[j] < stone[i]:
#                 step_l[i] = max(step_l[i], step_l[j] + 1)
#
#             if stone[n - j - 1] < stone[n - i - 1]:
#                 step_r[n - i - 1] = max(step_r[n - i - 1], step_r[n - j - 1] + 1)
#     result = [l + r for l, r in zip(step_r, step_l)]
#     print(max(result) - 1)
