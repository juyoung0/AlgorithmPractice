def solution(n, wires):
    answer = 100

    # 간선 하나씩 제거해보기
    for i in range(n - 1):
        node = [0 for _ in range(n + 1)]
        _wires = wires[:i] + wires[i + 1:]
        init = True
        group_id = 1
        # 각 그룹의 차이 재기
        for _w in _wires:
            if node[_w[0]] == node[_w[1]] and node[_w[0]] == 0:
                if init == True:
                    node[_w[0]] = group_id
                    node[_w[1]] = group_id
                    init = False
                else:
                    node[_w[0]] = group_id
                    node[_w[1]] = group_id
                group_id += 1
            elif node[_w[0]] == 0:
                node[_w[0]] = node[_w[1]]
            elif node[_w[1]] == 0:
                node[_w[1]] = node[_w[0]]
            else:
                if node[_w[0]] > node[_w[1]]:
                    node[_w[0]] = node[_w[1]]
                else:
                    node[_w[1]] = node[_w[0]]

        diff = abs((n - node[1:].count(1)) - node[1:].count(1))
        answer = min(answer, diff)

    return answer