import math
def solution(word):
    order = {'A':1, 'E':2, 'I':3, 'O':4, 'U':5}
    answer = 0
    for i, w in enumerate(word):
        answer += order[w]
        answer += sum([math.pow(5, j) for j in range(4-i, 0, -1)]) * (order[w] - 1)
    return answer

# 수열 다 만드는 방법
# from itertools import product
#
# solution = lambda word: sorted(["".join(c) for i in range(5) for c in product("AEIOU", repeat=i+1)]).index(word) + 1