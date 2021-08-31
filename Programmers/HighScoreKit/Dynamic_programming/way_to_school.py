# 210829 : 30분 소요
# 최단 경로 갯수 세는 것이 아닌, 최단 경로 세는 것인 줄 알고 초반에 코드 잘못 짬

def solution(m, n, puddles):
    answer = 0
    route = [[0] * (m + 1) for i in range(n + 1)]
    puddle = [[0] * (m + 1) for i in range(n + 1)]

    # 경로 지도 출발지 초기화.
    for p in puddles:
        puddle[p[1]][p[0]] = -1
    route[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 출발지 및 물웅덩이가 아니라면, top과 left 중 더 짧은 거리를 선택
            if not (i == 1 and j == 1) and puddle[i][j] != -1:
                route[i][j] = route[i-1][j] + route[i][j-1]

    answer = (route[n][m]) % 1000000007
    return answer

print(solution(2, 2, []), 2)
print(solution(3, 3, []), 6)
print(solution(3, 3, [[2, 2]]), 2)
print(solution(3, 3, [[2, 3]]), 3)
print(solution(3, 3, [[1, 3]]), 5)
print(solution(3, 3, [[1, 3], [3, 1]]), 4)
print(solution(3, 3, [[1, 3], [3, 1], [2, 3]]), 2)
print(solution(3, 3, [[1, 3], [3, 1], [2, 3], [2, 1]]), 1)
print(solution(7, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]), 0) # 이 값이 잘 나오면 테스트1, 테스트9 통과, 위로 가면 안됨
print(solution(4, 4, [[3, 2], [2, 4]]), 7)
print(solution(100, 100, []), 690285631)