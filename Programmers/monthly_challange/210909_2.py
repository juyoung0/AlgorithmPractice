def solution(grid):
    start = [[0, -1], [-1, 0], [0, 1], [1, 0]] #right, down, left, up
    R = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}
    L = {(0, 1): (1, 0), (1, 0): (0, 1), (0, -1): (-1, 0), (-1, 0): (0, -1)}
    S = {(0, 1): (0, 1), (1, 0): (1, 0), (0, -1): (0, -1), (-1, 0): (-1, 0)}
    answer = []
    strings = []
    skip = []
    for s in start:
        way = []
        way_n = ''
        cycle = False
        cur = [0, 0]
        prev_dir_x = 0 - s[0]
        prev_dir_y = 0 - s[1]
        start = True
        if s not in skip:
            while not cycle:
                # 시작점일 경우 탐색 안해도 되는 방향 제외
                if cur == [0, 0] and (0 - prev_dir_x, 0 - prev_dir_y) not in skip:
                    skip.append([0 - prev_dir_x, 0 - prev_dir_y])

                if grid[cur[0]][cur[1]] == 'S':
                    next_dir = S[(prev_dir_x, prev_dir_y)]
                    next = [cur[0] + next_dir[0], cur[1] + next_dir[1]]
                    dir_x = next_dir[0]
                    dir_y = next_dir[1]
                elif grid[cur[0]][cur[1]] == 'L':
                    next_dir = L[(prev_dir_x, prev_dir_y)]
                    next = [cur[0] + next_dir[0], cur[1] + next_dir[1]]
                    dir_x = next_dir[0]
                    dir_y = next_dir[1]
                else:
                    next_dir = R[(prev_dir_x, prev_dir_y)]
                    next = [cur[0] + next_dir[0], cur[1] + next_dir[1]]
                    dir_x = next_dir[0]
                    dir_y = next_dir[1]

                next[0] = next[0] % len(grid)
                next[1] = next[1] % len(grid[0])
                if next[0] == -1: next[0] = len(grid) - 1
                if next[1] == -1: next[1] = len(grid[1]) - 1

                if ((dir_x, dir_y), cur, next) in way:
                    cycle = True
                    #answer.append(way)
                else:
                    if start:
                        start = False
                    else:
                        way.append(((dir_x, dir_y), cur, next))
                    way_n += grid[cur[0]][cur[1]]

                    cur = next
                    prev_dir_x = dir_x
                    prev_dir_y = dir_y
            strings.append(way_n)


    for a in strings:
        answer.append(len(a) - 1)
    answer.sort()
    return answer

print(solution(["SL", "LR"]), [16])
print(solution(["S"]), [1, 1, 1, 1])
print(solution(["R", "R"]), [4, 4])
