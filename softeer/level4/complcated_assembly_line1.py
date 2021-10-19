# 최댓값을 설정할때 정확한 수치를 모르겠으면 그냥 inf 로 설정하자

import sys

K, N = map(int, input().split())
time = [[float('inf') for _ in range(N)] for _ in range(K)]

if N == 1:
    times = list(map(int, sys.stdin.readline().split()))
    print(min(times))
elif K == 1:
    answer = 0
    answer += sum([int(sys.stdin.readline()) for _ in range(N)])
    print(answer)
else:
    data = list(map(int, sys.stdin.readline().split()))
    prev_t = [[] for _ in range(K)]

    for i in range(K):
        time[i][0] = data[i]
    t = data[K:]
    for i in range(K):
        prev_t[i] = t[(K - 1) * i: (K - 1) * (i + 1)]
    for j in range(1, N):
        data = list(map(int, sys.stdin.readline().split()))

        # i 라인의 최소값 구하기. k에서 i로 넘어오는 경우도 고려함.
        for i in range(K):
            for k in range(K):
                if i != k:
                    prev = prev_t[k][i] if i < k else prev_t[k][i - 1]
                else:
                    prev = 0
                time[i][j] = min(time[k][j - 1] + prev + data[i], time[i][j])

        if j != N - 1:
            t = data[K:]
            for i in range(K):
                prev_t[i] = t[(K - 1) * i: (K - 1) * (i + 1)]

    answer = float('inf')
    for k in range(K):
        answer = min(answer, time[k][N - 1])
    print(answer)