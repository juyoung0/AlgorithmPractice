# 210829: 40분 소요.
# 반례 케이스를 잘 생각해 볼 것 (출발지가 될 수 없는 공항이 있음)
from collections import defaultdict

airports = defaultdict(list)

def dfs(airport, used, ticket_cnt):
    answer = [airport]

    if ticket_cnt == 0:
        return answer

    # 다른 곳 방문할 수 없는 경우
    # 1. 여기서 출발할 수 있는 티켓이 없음
    # 2. 여기서 출발할 수 있는 티켓은 있지만 이미 다 사용함
    if airport not in airports or 0 not in used[airport]:
        return False
    else:
        # 방문 가능한 곳 순차적으로 확인해보기
        dest = used[airport].index(0)

        for i in range(used[airport].count(0)):
            used[airport][dest + i] = 1
            route = dfs(airports[airport][dest + i], used, ticket_cnt - 1)
            if route:
                answer.extend(route)
                return answer
            else:
                used[airport][dest + i] = 0

    return False


def solution(tickets):
    answer = []
    global airports
    used = defaultdict(list)
    ticket_cnt = len(tickets)

    for ticket in tickets:
        airports[ticket[0]].append(ticket[1])
        airports[ticket[0]].sort()
        used[ticket[0]].append(0)

    route = dfs('ICN', used, ticket_cnt)
    if route:
        answer.extend(route)

    return answer

# 다른 풀이
# def solution(tickets):
#     routes = {}
#     for t in tickets:
#         routes[t[0]] = routes.get(t[0], []) + [t[1]]
#     for r in routes:
#         routes[r].sort(reverse=True)
#     stack = ["ICN"]
#     path = []
#     while len(stack) > 0:
#         top = stack[-1]
#         if top not in routes or len(routes[top]) == 0:
#             path.append(stack.pop())
#         else:
#             stack.append(routes[top][-1])
#             routes[top] = routes[top][:-1]
#     return path[::-1]