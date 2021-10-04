# 프로그래머 직업군 추천. 코드 간소화 진행

def solution(table, languages, preference):
    result_dict = {}

    for t in table:
        t = t.split(' ')
        score = [p * (5 - t[1:].index(l)) if l in t[1:] else 0 for p, l in zip(preference, languages)]
        result_dict[t[0]] = sum(score)
    answer = max(sorted(list(result_dict.keys())), key=(lambda key: result_dict[key]))
    return answer

# def solution(table, languages, preference):
#     lang_dict, result_dict = {}, {}
#     answer, max_val = '', 0
#     for t in table:
#         t = t.split(' ')
#         lang_dict[t[0]] = t[1:]
#         result_dict[t[0]] = 0
#
#     for key in lang_dict.keys():
#         for i, lang in enumerate(languages):
#             if lang in lang_dict[key]:
#                 result_dict[key] += preference[i] * (len(lang_dict[key]) - lang_dict[key].index(lang))
#
#         if result_dict[key] > max_val:
#             max_val = result_dict[key]
#             answer = key
#
#     answer = max(sorted(list(result_dict.keys())), key=(lambda key: result_dict[key]))
#     return answer