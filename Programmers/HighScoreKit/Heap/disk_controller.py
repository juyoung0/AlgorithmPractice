# 210829 : 30분 소요
# 결과에 int를 해주어야함

import heapq

def solution(jobs):
    answer = 0
    heap = []
    work = []
    curr_time = 0

    for job in jobs:
        heapq.heappush(heap, tuple(job))

    while len(heap) != 0:
        candi = []
        # 현재 가능한 작업들 뽑기. 소요시간을 앞에 넣어서 candi 중 최소 소요 시간을 뽑을 수 있게 함
        while len(heap) != 0 and heap[0][0] <= curr_time:
            pop = heapq.heappop(heap)
            heapq.heappush(candi, (pop[1], pop[0]))
        # 시간이 가장 적게 걸리는 작업 먼저 처리
        if len(candi) == 0:
            curr_time += 1
        else:
            curr_job = heapq.heappop(candi)
            curr_time += curr_job[0]
            work.append(curr_time - curr_job[1])
        # 남은 작업은 다시 heap에 넣어주기
        for c in candi:
            heapq.heappush(heap, (c[1], c[0]))

    return int(sum(work)/len(work))

print(solution([[0, 3], [1, 9], [2, 6]]), 9)
print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]), 74)
print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]), 72)