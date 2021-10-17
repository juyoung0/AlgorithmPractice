# super virus 방식으로 풀면 더 오래걸림. virus 방식으로 풀어야함
import sys

P, N = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

answer = 0
for i in range(N-1):
    answer = ((answer + data[i]) * P) % 1000000007
answer += data[-1]

print(answer % 1000000007)