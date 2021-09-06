# 210906: 1시간 소
from collections import defaultdict
from itertools import combinations

def solution(relation):
    key_num = len(relation[0])
    keys = defaultdict(list)
    unique_key = []
    for r in relation:
        for k in range(key_num):
            keys[str(k)].append(r[k])

    def check_key(key):
        # 최소성 조건 만족하는지 체크
        for u in unique_key:
            if len(set(key) - set(u)) == len(key) - len(u):
                return False
        # 유일성 조건 만족하는지 체크
        if len(key) == 1:
            if len(keys[key[0]]) == len(set(keys[key[0]])):
                return True
        else:
            temp = []
            for i in range(len(relation)):
                value = ''
                for k in key:
                    value += keys[str(k)][i]
                temp.append(value)
            if len(temp) == len(set(temp)):
                return True
        return False

    # 1...n 길이의 모든 조합 중 unique 키를 찾는다
    relation_key = list(keys.keys())
    not_unique_key = []
    for i in range(key_num):
        not_unique_key.extend(list(combinations(relation_key, i+1)))

    for key in not_unique_key:
        if check_key(key):
            unique_key.append(key)

    return len(unique_key)

print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]), 2)

# 유사한 코드 참고
# from collections import deque
# from itertools import combinations
# 
# def solution(relation):
#     n_row = len(relation)
#     n_col = len(relation[0])  # ->runtime error 우려되는 부분
#
#     candidates = []
#     for i in range(1, n_col + 1):
#         candidates.extend(combinations(range(n_col), i))
#
#     final = []
#     for keys in candidates:
#         tmp = [tuple([item[key] for key in keys]) for item in relation]
#         if len(set(tmp)) == n_row:
#             final.append(keys)
#     answer = set(final[:])
#
#     for i in range(len(final)):
#         for j in range(i + 1, len(final)):
#             if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
#                 answer.discard(final[j])
#
#     return len(answer)