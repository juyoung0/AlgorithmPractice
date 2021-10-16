# 재귀 방식으로 풀어야함 2^N -> logN

import sys

if __name__=="__main__":
    k, p, N = map(int, sys.stdin.readline().split())

    def calc(n):
        if n == 1:
            return p
        if n % 2 == 0:
            a = calc(n//2)
            return (a * a) % 1000000007
        else:
            a = calc(n//2)
            return (p * a * a) % 1000000007

    print(k * calc(N*10) % 1000000007)