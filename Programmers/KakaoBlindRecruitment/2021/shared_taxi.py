#210904 : 60분 소요
# 다익스트라 알고리즘 (우선순위 큐 활용)
from queue import PriorityQueue
from collections import defaultdict

def solution(n, s, a, b, fares):
    adj = defaultdict(list)
    pq = PriorityQueue()
    costs = [[0 for x in range(n+1)] for y in range(n+1)]
    answer = 100000 * n + 1

    for fare in fares:
        costs[fare[0]][fare[1]] = fare[2]
        costs[fare[1]][fare[0]] = fare[2]
        adj[fare[0]].append(fare[1])
        adj[fare[1]].append(fare[0])

    def dijkstra(start):
        dist = [(100000 * n + 1) for x in range(n + 1)]
        pq.put((0, start))
        dist[start] = 0
        while not pq.empty():
            node = pq.get()
            here = node[1]
            cost = node[0]
            # 더 싼 경로를 알고 있다면 Pass
            if dist[here] < cost: continue

            # 인접한 정점들을 모두 검사한다
            for there in adj[here]:
                next_dist = costs[here][there] + cost
                if next_dist < dist[there]:
                    dist[there] = next_dist
                    pq.put((next_dist, there))

        return dist

    dist = dijkstra(s)
    for i in range(1, n+1):
        dist_after = dijkstra(i)
        answer = min(answer, dist[i] + dist_after[a] + dist_after[b])

    print(fares)
    return adj

print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]), 14)
print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]), 18)
print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]), 82)

# 플로이드-워셜 알고리즘
# import heapq
#
# def solution(n, s, a, b, fares):
#     d = [ [ 20000001 for _ in range(n) ] for _ in range(n) ]
#     for x in range(n):
#         d[x][x] = 0
#     for x, y, c in fares:
#         d[x-1][y-1] = c
#         d[y-1][x-1] = c
#
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 if d[j][k] > d[j][i] + d[i][k]:
#                     d[j][k] = d[j][i] + d[i][k]
#
#     minv = 40000002
#     for i in range(n):
#         minv = min(minv, d[s-1][i]+d[i][a-1]+d[i][b-1])
#     return minv