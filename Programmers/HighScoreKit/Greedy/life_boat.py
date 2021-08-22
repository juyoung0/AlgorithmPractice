from collections import deque

def solution(people, limit):
    people_q = deque(sorted(people, reverse=True))
    answer = 0

    while len(people_q) > 1:
        answer += 1
        left = limit - people_q.popleft()
        if people_q[-1] <= left:
            people_q.pop()

    if len(people_q) == 1:
        answer += 1

    return answer