# 210906 : 2시간 정도 소요
# 효율성을 위한 로직은 생각했으나 curr_i를 계속 기억하도록 코드를 짜는 바람에 삽질
# 리스트에서 삭제가 이루어지는 와중에 인덱스를 기억하는 것은 리스크가 매우 크다

import heapq

def solution(food_times, k):
    foods = []
    for i, food in enumerate(food_times):
        heapq.heappush(foods, (food, i))
    prev_time = 0
    while True:
        N = len(foods)
        if N == 0:
            return -1
        food = foods[0]

        spare = (food[0] - prev_time) * N
        if k < spare:
            curr_i = k % len(foods)
            foods.sort(key=lambda x: x[1])
            return foods[curr_i][1] + 1
        else:
            k -= spare
            prev_time = food[0]
            heapq.heappop(foods)

    return 0

print(solution([3, 1, 2], 5), 1)
print(solution([4,2,3,6,7,1,5,8], 16), 3)
print(solution([4,2,3,6,7,1,5,8], 27), 5)
