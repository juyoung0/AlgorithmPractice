# 플로이드-워셜 알고리즘

def solution(n, results):
    answer = 0
    # 승리 횟수, 패배 횟수 저장
    adj = [[0 for i in range(n + 1)] for i in range(n + 1)]
    for r in results:
        win, lose = r[0], r[1]
        adj[win][lose] = 1
        adj[lose][win] = -1

    for i in range(n):
        adj[i][i] = 0

    # i->j 로 가는 경로는, i->j 직접 가는 것과 i->k->j 경유하는 것이 있다
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i != j and adj[i][j] == 0:
                    if adj[i][k] + adj[k][j] > 1:
                        route = 1
                    elif adj[i][k] + adj[k][j] < -1:
                        route = -1
                    else:
                        route = 0
                    adj[i][j] = adj[i][j] or route

    # 버리는 첫번째 인덱스, 그리고 자기자신 포함해서 0이 2개 뿐이면
    # 나머지 노드와의 순위는 알고 있다는 뜻이다
    for a in adj:
        if a.count(0) == 2:
            answer += 1
    return answer