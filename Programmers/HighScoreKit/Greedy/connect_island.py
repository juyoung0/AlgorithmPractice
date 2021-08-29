# 210829 : 1시간 소요
# Kruskal Algorithm : Minumum Spanning Tree
# Union Find Algoritihm

def solution(n, costs):
    # 비용이 낮은 순서대로 정렬
    costs.sort(key=lambda x: x[2])
    # cycle 되는 네트워크 유무를 감지하기 위함
    root_node = [i for i in range(n)]
    network = {i: [i] for i in range(n)}
    total_cost = 0

    for i, cost in enumerate(costs):
        a, b = cost[0], cost[1]

        # 서로 같은 네트워크 상에 있으면 다리를 놓을 필요 없음
        if root_node[a] != root_node[b]:
            total_cost += cost[2]

            if i == 0: # 최초 네트워크
                if a <= b :
                    network[a].append(b)
                    network[b] = []
                else :
                    network[b].append(a)
                    network[a] = []

                root_node[a] = min(a, b)
                root_node[b] = min(a, b)
            else:
                root_a = root_node[a]
                root_b = root_node[b]
                min_r, max_r = min(root_a, root_b), max(root_a, root_b)

                # 두 네트워크 합치기
                network[min_r].extend(network[max_r])
                for n in network[max_r]:
                    root_node[n] = min_r
                network[max_r] = []

    return total_cost

print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]), 4)
print(solution(5, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]]), 15)
print(solution(5, [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]]), 8)
print(solution(4, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]]), 9)
print(solution(5, [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]]), 104)
print(solution(6, [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]), 11)
print(solution(5, [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]]), 104)
# #
# 5 [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]] 15
# 5 [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]] 8
# 4 [[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]] 9
# 5 [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]] 104
# 6 [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]] 11
# 5 [[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]] 6
# 5 [[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]] 8
# 5 [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 3, 1]] 8