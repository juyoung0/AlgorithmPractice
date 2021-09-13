# 길이가 긴 리스트이고, 최대/최소 값을 물어볼 경우
# 이분탐색으로 접근한다

def check(stones, k, N):
    gap = 0
    for s in stones:
        if s <= N:
            gap += 1
        else:
            gap = 0
        if gap == k:
            return False
    return True

def solution(stones, k):
    if len(stones) == 1:
        return stones[0]
    if k == 1:
        return min(stones)
    left, right = 0, 200000000
    while left <= right:
        mid = (left + right)//2
        if check(stones, k, mid):
            left = mid + 1
        else:
            right = mid - 1

    return left