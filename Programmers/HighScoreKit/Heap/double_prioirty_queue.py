# 210903: 15분 소요
# min heap은 queue[0]이 최솟값인건 보장해주지만, queue[-1]가 최댓값인건 보장해주지 않는다
# max(queue) 을 통해 최댓값을 구했다 => 만약 시간초과가 난다면 maxheap 도 같이 관리해주어야 한다

import heapq

def solution(operations):
    queue = []

    for opr in operations:
        print(queue)
        if opr[0] == 'I':
            heapq.heappush(queue, int(opr[1:]))
        else:
            if len(queue) != 0:
                if opr[2:] == '-1':
                    heapq.heappop(queue)
                else:
                    queue = queue[:-1]

    if len(queue) == 0:
        return [0, 0]
    return [queue[-1], queue[0]]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]), [0, 0])
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]), [333, -45])
print(solution(["I 10000", "D -1", "I 4", "I 3", "I 2", "I 1"]), [4, 1])