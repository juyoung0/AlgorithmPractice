# 210906: 20분 소요

def solution(N, stages):
    stages.sort()
    failure = []  # stage, failure 저장

    s = 0
    total = len(stages)
    for i in range(1, N + 1):
        cnt = 0
        while s < len(stages) and stages[s] == i:
            cnt += 1
            s += 1
        if total != 0:
            failure.append((i, cnt / total))
        else:
            failure.append((i, 0))
        print(i, total, cnt)
        total -= cnt

    failure.sort(reverse=True, key=lambda x: x[1])
    return [f[0] for f in failure]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]), [3, 4, 2, 1, 5])
print(solution(5, [1, 1, 1]), [1, 2, 3, 4, 5])