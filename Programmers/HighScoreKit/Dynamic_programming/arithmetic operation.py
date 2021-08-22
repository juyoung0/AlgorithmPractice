def solution(N, number):
    # memoization 을 위한 배열 생성. 8번을 최대 횟수로 지정
    memo = [[] for _ in range(9)]
    memo[1] = [N]
    cnt = 1
    n = N
    if number == N:
        return 1

    while cnt < 8:
        cnt += 1
        n = int(str(n) + str(N))
        if n == number:
            return cnt
        memo[cnt].append(n)

        for c in range(cnt):
            for i in list(set(memo[c])):
                for j in list(set(memo[cnt-c])):
                    memo[cnt].append(i + j)
                    memo[cnt].append(i - j)
                    memo[cnt].append(j - i)
                    memo[cnt].append(i * j)
                    if i != 0:
                        memo[cnt].append(j / i)
                    if j != 0:
                        memo[cnt].append(i / j)

            if number in memo[cnt]:
                return cnt

    return -1

if __name__ == '__main__':
    print(solution(8, 5800))