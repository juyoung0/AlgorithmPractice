# 카카오 디딤돌
# 리스트 접근방식으로 풀어서 정확도는 만점이지만 효율성은 틀림
# 이진탐색으로 접근해야 할 듯

from collections import deque
import re

def solution(stones, k):
    answer = 0
    empty_check = ['1' for _ in range(len(stones))]
    pair = [(s, i) for i, s in enumerate(stones)]
    pair.sort(key=lambda x: x[0])
    pair_q = deque(pair)
    while len(pair_q) > 0:
        min_val = pair_q[0][0]
        poss = min_val - answer
        pop_cnt = 0
        empty = []

        while pair_q[0][0] == min_val:
            empty_check[pair_q[0][1]] = '0'
            empty.append(pair_q.popleft()[1])
            break
        answer += poss
        p = re.compile(r'0{'+str(k)+r'}')

        for e in empty:
            s_i = e - k if e-k>=0 else 0
            f_i = e + k if e+k<len(empty_check) else len(empty_check) - 1

            if p.search(''.join(empty_check[s_i:f_i+1])):
                return answer
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3), 3)
