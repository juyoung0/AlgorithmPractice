from collections import deque

def check_diff(a, b):
    diff = len(a)
    for i in range(len(a)):
        if a[i] == b[i]:
            diff -= 1

    if diff == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    if target not in words:
        return 0

    word_network = [[0] * 50 for i in range(50)]
    words = [begin] + words
    route = deque()
    visited = []
    answer = 51

    # 네트워크 만들기
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if check_diff(words[i], words[j]):
                word_network[i][j] = 1
                word_network[j][i] = 1

    # bfs 시작하기 => 최단경로 찾으면 바로 return 할 수 있도록
    for i in word_network[0]:
        route.append(i)
        depth = 0
        if i not in visited:
            next_route = [j for j, x in enumerate(word_network[i]) if x == 1]

            while True:
                route = next_route
                next_route = []
                depth += 1
                while len(route) != 0:
                    node = route.pop()
                    visited.append(node)

                    # target 에 도착
                    if words[node] == target:
                        return depth

                    next_words = [j for j, x in enumerate(word_network[node]) if x == 1]

                    # 아직 갈 길이 있다면 남은 길 탐색
                    left_route = list(set(next_words) - set(visited))
                    next_route.extend(left_route)

    return 0


if __name__ == "__main__":
    solution("hit", "cog", ["cog", "log", "lot", "dog", "dot", "hot"])
    solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])