# numpy 안 쓰고 행렬 바꾸는 팁
#  scores = list(map(list, zip(*scores)))

def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'


def solution(scores):
    answer = []

    scores_r = [[] for _ in range(len(scores))]
    for score in scores:
        for i, s in enumerate(score):
            scores_r[i].append(s)

    for i in range(len(scores)):
        if (scores_r[i][i] == max(scores_r[i]) or scores_r[i][i] == min(scores_r[i])) and scores_r[i].count(
                scores_r[i][i]) == 1:
            answer.append(grade((sum(scores_r[i]) - scores_r[i][i]) / (len(scores) - 1)))
        else:
            answer.append(grade(sum(scores_r[i]) / len(scores)))
    return "".join(answer)


# 다른 사람 코드 1
# def solution(scores):
#     answer = ''
#
#     for i, score in enumerate(zip(*scores)):
#         avg = (sum(score) - score[i]) / (len(score) - 1) if score[i] in (min(score), max(score)) and score.count(score[i]) == 1 else sum(score) / len(score)
#         answer += "%s" % (
#             "A" if 90 <= avg else
#             "B" if 80 <= avg else
#             "C" if 70 <= avg else
#             "D" if 50 <= avg else
#             "F"
#         )
#
#     return answer

# 다른 사람 코드 2
# solution = lambda scores: "".join(map(lambda m: "FDDCBAA"[max(int(sum(m) / len(m) / 10) - 4, 0)], map(lambda m: (m[0], *m[1]) if min(m[1]) <= m[0] <= max(m[1]) else m[1], ((s[i], s[:i] + s[i+1:]) for i, s in enumerate(zip(*scores))))))
