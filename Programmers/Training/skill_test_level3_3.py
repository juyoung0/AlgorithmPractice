# 효진이 멀리뛰기 문제

def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    step = [0 for _ in range(n)]
    step[0] = 1
    step[1] = 2
    step[2] = (step[0]) + (step[1])

    for i in range(3, n):
        step[i] = (step[i - 2]) + (step[i - 1])

    answer = step[n - 1] % 1234567
    return answer