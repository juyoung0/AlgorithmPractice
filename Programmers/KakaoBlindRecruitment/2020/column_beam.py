# 210905: 1시간 30분 소요

def solution(n, build_frame):
    answer = []
    frame = [[[0, 0] for _ in range(n + 1)] for _ in range(n + 1)]  # 기둥, 보 순서

    def check_column_insert(x, y):
        # 해당 위치에 이미 설치되어 있음
        if frame[x][y][0] == 1:
            return False

        # 설치하려는 곳이 바닥, 보의 끝, 기둥 위인지 확인
        if y == 0 or frame[x][y - 1][0] == 1 or frame[x][y][1] == 1 or (x > 0 and frame[x - 1][y][1] == 1):
            return True

        return False

    def check_beam_insert(x, y):
        # 해당 위치에 이미 설치되어 있음
        if frame[x][y][1] == 1:
            return False

        if ((y > 0 and frame[x][y - 1][0] == 1) or frame[x + 1][y - 1][0] == 1) or (
                (x > 0 and frame[x - 1][y][1] == 1) and (x < n and frame[x + 1][y][1] == 1)):
            return True

        return False

    def check_column_delete(x, y):
        # 기둥을 삭제하면, 기둥 위쪽의 보(왼/오)와 기둥이 조건에 부합하는지 확인해주어야함
        delete(x, y, 0)
        # 바로 위의 기둥
        if frame[x][y + 1][0] == 1:
            delete(x, y + 1, 0)
            if not check_column_insert(x, y + 1):
                insert(x, y, 0)
                insert(x, y + 1, 0)
                return False
            insert(x, y + 1, 0)

        # 바로 위의 보 (오른쪽)
        if frame[x][y + 1][1] == 1:
            delete(x, y + 1, 1)
            if not check_beam_insert(x, y + 1):
                insert(x, y, 0)
                insert(x, y + 1, 1)
                return False
            insert(x, y + 1, 1)

        # 바로 위의 보 (왼쪽))
        if x > 0:
            if frame[x - 1][y + 1][1] == 1:
                delete(x - 1, y + 1, 1)
                if not check_beam_insert(x - 1, y + 1):
                    insert(x, y, 0)
                    insert(x - 1, y + 1, 1)
                    return False
                insert(x - 1, y + 1, 1)

        insert(x, y, 0)
        return True

    def check_beam_delete(x, y):
        # 보를 삭제하면, 보 양쪽 끝의 보와 기둥이 조건에 부합하는지 확인해주어야함
        delete(x, y, 1)

        # 왼쪽의 기둥 검사하기
        if frame[x][y][0] == 1:
            delete(x, y, 0)
            if not check_column_insert(x, y):
                insert(x, y, 1)
                insert(x, y, 0)
                return False
            insert(x, y, 0)

        # 왼쪽의 보 검사하기
        if x > 0 and frame[x - 1][y][1] == 1:
            delete(x - 1, y, 1)
            if not check_beam_insert(x - 1, y):
                insert(x, y, 1)
                insert(x - 1, y, 1)
                return False
            insert(x - 1, y, 1)

        # 오른쪽 기둥 검사하기
        if frame[x + 1][y][0] == 1:
            delete(x + 1, y, 0)
            if not check_column_insert(x + 1, y):
                insert(x, y, 1)
                insert(x + 1, y, 0)
                return False
            insert(x + 1, y, 0)

        # 오른쪽 보 검사하기
        if x < n and frame[x + 1][y][1] == 1:
            delete(x + 1, y, 1)
            if not check_beam_insert(x + 1, y):
                insert(x, y, 1)
                insert(x + 1, y, 1)
                return False
            insert(x + 1, y, 1)

        insert(x, y, 1)
        return True

    def insert(x, y, a):
        frame[x][y][a] = 1

    def delete(x, y, a):
        frame[x][y][a] = 0

    for build in build_frame:
        if build[3] == 1:
            if build[2] == 0:
                if check_column_insert(build[0], build[1]):
                    insert(build[0], build[1], build[2])
            else:
                if check_beam_insert(build[0], build[1]):
                    insert(build[0], build[1], build[2])
        else:
            if build[2] == 0:
                if check_column_delete(build[0], build[1]):
                    delete(build[0], build[1], build[2])
            else:
                if check_beam_delete(build[0], build[1]):
                    delete(build[0], build[1], build[2])

    for i in range(n + 1):
        for j in range(n + 1):
            for k in range(2):
                if frame[i][j][k] == 1:
                    answer.append([i, j, k])
    return answer

print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]), [[1, 0, 0], [1, 1, 1], [2, 1, 0], [2, 2, 1], [3, 2, 1], [4, 2, 1], [5, 0, 0], [5, 1, 0]])