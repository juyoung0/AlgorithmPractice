from collections import deque

def solution(n, computers):
    answer = 0
    computer_q = deque()
    visited = [0] * n

    for node in range(n):
        computer_q.append(node)

        if visited[node] == 0:
            while len(computer_q) > 0:
                j = computer_q.popleft()
                visited[j] = 1
                connected = [i for i, x in enumerate(computers[j]) if x == 1]
                computer_q.extend(connected)
                computers[j] = [0] * n

            answer += 1

    return answer