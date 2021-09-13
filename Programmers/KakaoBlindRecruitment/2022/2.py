def is_prime(num):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
    else:
        return False
    return True


def solution(n, k):
    answer = 0
    changed = ""
    if n == 1:
        return 0

    if n // k < 1:
        changed = str(n)
    else:
        while n > 1:
            n, mod = divmod(n, k)
            changed += str(mod)
        if n == 1:
            changed += str(n)
        changed = changed[::-1]

    nums = changed.split('0')

    # 소수 목록 만들기
    #     m = 2000000
    #     a = [False,False] + [True]*(m-1)
    #     primes=[]

    #     for i in range(2,int(m ** 0.5)+1):
    #         if a[i]:
    #             primes.append(i)
    #         for j in range(2*i, m+1, i):
    #             a[j] = False

    for num in nums:
        if len(num) > 0:
            if int(num) != 1:
                # if int(num) in primes:
                #     answer += 1
                # if int(num) > m:
                #     answer += 1
                if is_prime(int(num)):
                    answer += 1
    return answer

#print(solution(437674, 7), 3)
#print(solution(110011, 10), 2)
print(solution(1000000, 3), 0)
#print(solution(999998, 3), 0)