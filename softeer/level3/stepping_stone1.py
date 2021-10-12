# O(N^2)

if __name__=="__main__":
    n = int(input())
    stone = list(map(int, input().split()))
    steps = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if stone[j] < stone[i]:
                steps[i] = max(steps[i], steps[j] + 1)
    print(max(steps))