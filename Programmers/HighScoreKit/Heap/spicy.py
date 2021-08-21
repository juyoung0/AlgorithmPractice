import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    done = False
    mix = 0

    while (not done):
        if len(scoville) == 1:
            if scoville[0] < K:
                return -1
            else:
                done = True
        else:
            if scoville[0] < K:
                a = heapq.heappop(scoville)
                b = heapq.heappop(scoville)
                heapq.heappush(scoville, a + (b * 2))
                mix += 1
            else:
                done = True

    answer = mix
    return answer