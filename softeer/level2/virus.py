import sys

if __name__=="__main__":
    k, p, n = map(int, sys.stdin.readline().split())
    answer = k
    for _ in range(n):
        answer = (answer * p) % 1000000007
    print(answer)