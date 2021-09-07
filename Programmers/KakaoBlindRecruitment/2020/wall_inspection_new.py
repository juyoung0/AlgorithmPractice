# 210907: 삽질 2시간, 새로 푸는데 1시간 반
# deque 는 리스트를 rotate 시킬 수 있다
# 회전하는 배열은 리스트를 두 배 늘려주는 방식으로 해결하자
import itertools
from collections import deque

def solution(n, weak, dist):
    cnt = len(weak)
    weak = deque(weak)
    dist.sort(reverse=True)
    # 원형 배열은 배열을 두 배 늘려주는 방식으로 많이 푼다
    for i in range(len(weak)):
       weak.append(weak[i] + n)

    # dist 가 큰 친구부터 차례대로 투입한다. 투입할 순서를 순열로 만든다
    for num in range(1, len(dist)+1):
        candis = itertools.permutations(dist[:num])
        # 출발 weak 지점의 위치를 한 칸씩 옮겨가며 검사한다
        for candi in candis:
            # n명의 친구들의 순서 조합
            # weak 한 칸씩 미루기
            for w in range(len(weak)):
                i, check = w, 0
                # 각 친구들을 검사하러 보낸다
                for c in candi:
                    left_step = c % n
                    while i < len(weak)-1 and check < cnt:
                        i += 1
                        if weak[i] - weak[i-1] <= left_step:
                            left_step -= (weak[i] - weak[i-1])
                            check += 1
                        else:
                            check += 1
                            break

                    if check == cnt:
                        print(c, i, weak[i], left_step, check)
                        return len(candi)

    return -1

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]), 2)
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]), 1)