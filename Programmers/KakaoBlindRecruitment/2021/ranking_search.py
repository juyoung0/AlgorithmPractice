# 210823 : 문제풀이 50분. 효율성 실패.
# set 비교 방식으로 구현했다가, dictionary 활용하는 방식으로 재코딩
from itertools import combinations
from collections import defaultdict
import bisect

def solution(info, query):
    answer = []
    infos = defaultdict(list)

    # 그룹 나누기
    for _i, _info in enumerate(info):
        vals = _info.split(' ')
        keys = vals[:4]
        for _j in range(len(keys) + 1):
            for _c in combinations(keys, _j):
                key = ''.join(list(_c))
                if key == '': key = 'all'

                if key in infos:
                    infos[key].append(int(vals[4]))
                else:
                    infos[key] = [int(vals[4])]

    # 점수 정렬하기
    for _key in infos.keys():
        infos[_key].sort()

    # 순서대로 쿼리하기
    for _q in query:
        vals = _q.split(' and ')
        vals[3], score = vals[3].split(' ')
        key = ''.join([v if v != '-' else '' for v in vals[:4]])
        if key == '': key = 'all'
        if key not in infos:
            answer.append(0)
        else:
            # 이진탐색으로 찾기
            if len(infos[key]) == 1:
                if infos[key][0] >= int(score):
                    answer.append(1)
                else:
                    answer.append(0)
            else:
                answer.append(len(infos[key]) - bisect.bisect_left(infos[key], int(score)))

    return answer

# def solution(info, query):
#     answer = []
#     infos = [[] for x in range(5)]
#
#     for i, _info in enumerate(info):
#         vals = _info.split(' ')
#         for j, v in enumerate(vals):
#             infos[j].append(v)
#
#     for _q in query:
#         vals = _q.split(' and ')
#         vals[3], score = vals[3].split(' ')
#         set_q = set(i for i in range(len(info)))
#
#         # 각 조건은 set으로 비교
#         for j, _v in enumerate(vals):
#             if _v != '-':
#                 indices = set([i for i, x in enumerate(infos[j]) if x == _v])
#                 set_q &= indices
#
#         # score 는 검색이 필요함 => 여기서 시간 초과 발생하므로 탐색 기법을 이분법으로 바꾸기
#         set_q &= set([i for i, x in enumerate(infos[4]) if int(x) >= int(score)])
#         answer.append(len(set_q))
#     return answer