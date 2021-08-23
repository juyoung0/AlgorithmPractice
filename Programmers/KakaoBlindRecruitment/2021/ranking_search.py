# 210823 : 문제풀이 50분. 효율성 실패.

def solution(info, query):
    answer = []
    infos = [[] for x in range(5)]

    for i, _info in enumerate(info):
        vals = _info.split(' ')
        for j, v in enumerate(vals):
            infos[j].append(v)

    for _q in query:
        vals = _q.split(' and ')
        vals[3], score = vals[3].split(' ')
        set_q = set(i for i in range(len(info)))

        # 각 조건은 set으로 비교
        for j, _v in enumerate(vals):
            if _v != '-':
                indices = set([i for i, x in enumerate(infos[j]) if x == _v])
                set_q &= indices

        # score 는 검색이 필요함 => 여기서 시간 초과 발생하므로 탐색 기법을 이분법으로 바꾸기
        set_q &= set([i for i, x in enumerate(infos[4]) if int(x) >= int(score)])
        answer.append(len(set_q))
    return answer