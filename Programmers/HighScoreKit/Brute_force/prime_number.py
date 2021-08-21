from itertools import permutations, combinations


def solution(numbers):
    elems = list(numbers)
    combs = []
    for i in range(len(elems)):
        combs += list(permutations(elems, i + 1))
    comb = list(set(map(lambda x: int(''.join(x)), combs)))
    comb = [x for x in comb if x not in [0, 1]]
    comb.sort()

    # 에라토스테네스의 체
    n = max(comb)
    primes = [True] * (n + 1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        # i가 소수인 경우 i이후 i의 배수들을 False 판정
        if primes[i] == True:
            for j in range(i + i, n + 1, i):
                primes[j] = False

    result = [x for x in comb if primes[x] == True]

    answer = len(result)
    return answer