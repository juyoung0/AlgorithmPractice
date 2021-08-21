from collections import deque

def solution(priorities, location):
    loc = location
    q = deque(priorities)
    answer = 0
    max_prior = max(list(q))

    while q:
        elem = q.popleft()
        if elem < max_prior:
            q.append(elem)
        else:
            answer += 1
            if loc == 0:
                break;

        loc = (loc - 1) % len(q)
        max_prior = max(list(q))

    return answer