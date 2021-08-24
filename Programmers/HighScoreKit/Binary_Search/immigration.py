# 0~최대시간 사이 임의의 시간이 최소시간이라 가정
# 이분탐색을 통해 최소시간 찾기
# 임의의 시간 내에 몇 명의 심사를 처리할 수 있는지 체크gi

def solution(n, times):
    times.sort()
    begin_i, end_i = times[0], times[0] * n + 1

    while begin_i <= end_i:
        finished = 0
        mid_i = (begin_i + end_i) // 2
        for time in times:
            finished += mid_i // time
            # finished 가 n을 초과한다면, 더 짧은 시간에도 가능하다는 뜻임
            if finished >= n:
                end_i = mid_i -1
                break;

        # finished 가 n 보다 작다면, 더 많은 시간이 필요함
        if finished < n:
            begin_i = mid_i + 1

    # 단 하나밖에 없는 답을 초반에 찾았을 경우, 아래쪽에서 탐색하다가 정답-1 에 머무름
    if finished < n:
        return mid_i + 1
    else:
        return mid_i

if __name__ == '__main__':
    solution(6, [7, 10])
    solution(3, [3, 3, 3])