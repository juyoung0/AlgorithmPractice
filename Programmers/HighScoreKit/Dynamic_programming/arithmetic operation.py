def solution(N, number):
    # memoization 을 위한 배열 생성. 9번을 최대 횟수로 지정
    # 각 index는 숫자를 나타내며, 값은 사용한 N의 갯수를 나타낸다
    memo = [9] * 32001
    memoed = []
    answer = 0
    cnt = 1
    n = N

    while True:
        if n == number:
            return min(cnt, memo[n])
        elif n <= 32000 and memo[n] > cnt:
            memo[n] = cnt
            memoed.append(n)

        temp = []
        for m in memoed:
            new_cnt = memo[m] + cnt
            if new_cnt > 8:
                return -1

            if m + n <= 32000:
                if new_cnt < memo[m + n]:
                    memo[m + n] = new_cnt
                    temp.append(m + n)

            if 32000 >= m - n >= 0:
                if new_cnt < memo[m - n]:
                    memo[m - n] = new_cnt
                    temp.append(m - n)

            if 32000 >= n - m >= 0:
                if new_cnt < memo[n - m]:
                    memo[n - m] = new_cnt
                    temp.append(n - m)

            if n * m <= 32000:
                if new_cnt < memo[n * m]:
                    memo[n * m] = new_cnt
                    temp.append(n * m)

            if n != 0 and m//n <= 32000:
                if new_cnt < memo[m // n]:
                    memo[m // n] = new_cnt
                    temp.append(m // n)

            if m != 0 and n//m <= 32000 :
                if new_cnt < memo[n // m]:
                    memo[n // m] = new_cnt
                    temp.append(n // m)

            print(m, n, memo[55])

        memoed.extend(temp)

        if memo[number] != 9:
            return memo[number]

        n = int(str(n) + str(number))
        cnt += 1

    return -1

if __name__ == '__main__':
    print(solution(5, 12))