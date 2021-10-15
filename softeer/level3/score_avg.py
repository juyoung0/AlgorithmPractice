n, k = map(int, input().split())
score = list(map(int, input().split()))
for _ in range(k):
    i, j = map(int, input().split())
    print(round(sum(score[i-1:j]) / (j-i+1), 2))