# 그냥 sort는 시간이 오래걸려서, 각 가치 당 무게를 카운팅하는 리스트르 따로 만듬
import sys

if __name__=="__main__":
    W, n = map(int, sys.stdin.readline().split())
    weight, value = 0, 0
    stuff = [0 for _ in range(10001)]
    for _ in range(n):
        a = list(map(int, input().split()))
        stuff[a[1]] += a[0]

    i = 10000
    while W > 0:
        if stuff[i] <= W:
            W -= stuff[i]
            value += stuff[i] * i
        else:
            value += W * i
            break
        i -= 1

    print(value)

# 변경 전
# if __name__=="__main__":
#     W, n = map(int, sys.stdin.readline().split())
#     weight, value = 0, 0
#     stuff = []
#     for _ in range(n):
#         a = list(map(int, input().split()))
#         stuff.append(a)
#
#     stuff.sort(key=lambda x: x[1], reverse=True)
#     for s in stuff:
#         if s[0] <= W:
#             W -= s[0]
#             value += s[0] * s[1]
#         else:
#             value += W * s[1]
#             break
#
#     print(value)