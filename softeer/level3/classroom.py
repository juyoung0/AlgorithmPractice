# deque로 하니 시간초과 남. heapq으로 수정함
# 그래도 시간초과
import sys
import heapq
import datetime
import random

if __name__=="__main__":
    n = 1000000 #int(input())
    heap = []
    for _ in range(n):
        # 강의가 끝나는 시간 순으로 정렬하기 위해 heap에 순서를 반대로 넣는다
        class_time = tuple(map(int, tuple(map(int, sys.stdin.readline().split()))))
        heapq.heappush(heap, (class_time[1], class_time[0]))

    time, cnt = 0, 0

    while heap:
        item = heapq.heappop(heap)
        # 강의 시작시간이 현재 시간보다 크거나 같으면 들을 수 있다
        if item[1] >= time:
            time = item[0]
            cnt += 1

    print(cnt)


# from collections import deque
#
# if __name__ == "__main__":
#     n = int(input())
#     temp = []
#     for _ in range(n):
#         temp.append(tuple(map(int, input().split())))
#     temp.sort(key=lambda x: x[1])
#     classes = deque(temp)
#
#     time, cnt = 0, 0
#     while classes:
#         time = classes.popleft()[1]
#         cnt += 1
#         while classes and classes[0][0] < time:
#             classes.popleft()
#
#     print(cnt)