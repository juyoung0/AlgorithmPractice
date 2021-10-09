import sys

if __name__=="__main__":
    n, m = map(int, sys.stdin.readline().split())
    limit, speed = [], []
    for _ in range(n):
        a = list(map(int, input().split()))
        limit += [a[1]] * a[0]

    for _ in range(m):
        a = list(map(int, input().split()))
        speed += [a[1]] * a[0]

    answer = max(speed[i] - limit[i] for i in range(len(speed)))
    print(0 if answer < 0 else answer)