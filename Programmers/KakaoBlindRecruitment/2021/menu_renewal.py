# 210823 : 풀이시간 50분

from collections import Counter
from itertools import combinations

def solution(orders, course):
    combi = [[] for c in range(len(course))]
    counter = [[] for c in range(len(course))]
    answer = []

    # 주문 별 조합 갯수 새기
    for order in orders:
        for i, c in enumerate(course):
            temp = list(combinations(order, c))
            for t in temp:
                t = sorted(list(t))
                combi[i].append(''.join(t))

    for i, c in enumerate(course):
        counter[i] = Counter(combi[i])

    # 각 조합 별 메뉴 선정하기
    for i, count in enumerate(counter):
        if count.values():
            highest = max(count.values())
        else:
            highest = 21
        for menu in count.keys():
            if count[menu] >= 2 and highest == count[menu]:
                answer.append(menu)

    answer = sorted(answer)
    return answer


# 다른 사람 풀이
# import collections
# import itertools
#
# def solution(orders, course):
#     result = []
#
#     for course_size in course:
#         order_combinations = []
#         for order in orders:
#             order_combinations += itertools.combinations(sorted(order), course_size)
#
#         most_ordered = collections.Counter(order_combinations).most_common()
#         result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]
#
#     return [ ''.join(v) for v in sorted(result) ]