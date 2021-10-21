import sys

K, N = map(int, input().split())
min_times = [float('inf') for _ in range(K)]

if N == 1:
    times = list(map(int, sys.stdin.readline().split()))
    print(min(times))
elif K == 1:
    answer = 0
    answer += sum([int(sys.stdin.readline().split()[0]) for _ in range(N)])
    print(answer)
else:
    data = list(map(int, sys.stdin.readline().split()))
    prev_t = data[-1]
    min_times = data[:K]
    min_time = min(min_times)
    for j in range(1, N):
        data = list(map(int, sys.stdin.readline().split()))
        min_times = [min(min_time + prev_t + d, min_times[i] + d) for i, d in enumerate(data[:K])]
        min_time = min(min_times)
        if j != N-1:
            prev_t = data[-1]

    answer = min(min_times)
    print(answer)