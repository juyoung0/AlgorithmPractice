from collections import deque
import math

def solution(progresses, speeds):
    days = deque()
    answer = []

    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])
        days.append(day)
    while (len(days) != 0):
        std_day = days.popleft()
        cnt = 1
        loop = True
        while (loop):
            if len(days) == 0:
                loop = False
            else:
                if days[0] <= std_day:
                    cnt += 1
                    days.popleft()
                else:
                    loop = False

        answer.append(cnt)
    return answer