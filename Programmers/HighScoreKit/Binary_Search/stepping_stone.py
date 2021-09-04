# 임의의 최소 거리를 이분탐색으로 탐색하며, 거리를 충족할 때 제거한 바위갯수가 N인지 확인한다

def solution(distance, rocks, N):
    answer = 0
    rocks.sort()
    left, right = 1, distance
    max_gap = 0

    while left <= right:
        prev, removed = 0, 0
        mid = (left + right) // 2
        for r in rocks:
            if r - prev < mid:
                removed += 1
                if removed > N: break;
            else:
                prev = r

        # 마지막 바위 지우는 경우도 확인
        if distance - prev < mid:
            removed += 1

        # 부순 개수가 N 이하일 경우 답이 될 수 있음
        if removed <= N:
            max_gap = max(mid, max_gap)
            left = mid + 1
        # 부순 개수가 N 보다 많을 경우, 간격을 줄여야 함
        elif removed > N:
            right = mid - 1

    return max_gap

print(solution(25, [2, 14, 11, 21, 17], 2), 4)
print(solution(16, [4, 8, 11], 2), 8)