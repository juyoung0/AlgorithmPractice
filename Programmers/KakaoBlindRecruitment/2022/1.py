from collections import defaultdict

def solution(id_list, _report, k):
    answer = []
    user = defaultdict(list)
    report = {}
    for r in _report:
        a, b = r.split(' ')
        user[b].append(a)

    for u in user.keys():
        if len(set(user[u])) >= k:

            for a in list(set(user[u])):
                if a not in report:
                    report[a] = 1
                else:
                    report[a] += 1
    answer = []
    for id in id_list:
        if id in report:
            answer.append(report[id])
        else:
            answer.append(0)
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2), [2, 1, 1, 0])