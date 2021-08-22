def solution(clothes):
    items = {}
    # 아이템 dict 만들기
    for cloth in clothes:
        if cloth[1] in items:
            items[cloth[1]].append(cloth[0])
        else:
            items[cloth[1]] = [cloth[0]]

    combi = 1
    # 선택하지 않는 것도 하나의 경우로 간주하여 모든 조합의 갯수 구함
    for item in items.keys():
        combi *= (len(items[item]) + 1)

    # 전부 안 걸치는 경우를 빼줌
    answer = combi - 1
    return answer

# 다른 코드 참고. Counter과 reduce 사용
# def solution(clothes):
#     from collections import Counter
#     from functools import reduce
#     cnt = Counter([kind for name, kind in clothes])
#     answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
#     return answer