# 210831 : DP 방식을 변경하여 런타임 에러 해결
def solution(money):
    if len(money) == 3:
        return len(money[0])

    # 첫번째 집을 털 경우
    memo = [-1 for x in range(len(money))]
    memo[0] = money[0]
    memo[1] = max(memo[0], memo[1])
    for i in range(2, len(memo) - 1):
        memo[i] = max(memo[i - 2] + money[i], memo[i - 1])
    answer_1 = memo[len(memo) - 2]

    # 첫번째 집을 털지 않을 경우
    memo = [-1 for x in range(len(money))]
    memo[0] = 0
    memo[1] = money[1]
    for i in range(2, len(memo)):
        memo[i] = max(memo[i - 2] + money[i], memo[i - 1])
    answer_2 = memo[len(memo) - 1]

    return max(answer_1, answer_2)

print(solution([1000, 1, 0, 1, 2, 1000, 0]), 2001)
print(solution([1, 4]), 4)
print(solution([4]), 4)

# 참고 : 다른 사람의 풀이
# def solution(money):
#     if len(money) == 3:
#         return max(money)
#     else:
#
#         with0 = [money[0], money[1], money[0] + money[2], max(money[0], money[1]) + money[3]]
#         wout0 = [money[1], money[2], money[1] + money[3]]
#         for m in money[4:]:
#             with0.append(max(with0[-2], with0[-3]) + m)
#             wout0.append(max(wout0[-2], wout0[-3]) + m)
#
#     return max(with0[-3], with0[-2], wout0[-1])

# DP 적용해서 일반 채점은 다 통과했으나, 효율성에서 런타임에러 발생
# def solution(money):
#     answer = 0
#     first_home = True
#     memo = [-1 for x in range(len(money))]
#
#     def DP(i):
#         if i >= len(money):
#             return 0
#         if i == len(money) - 1:
#             if first_home:
#                 return 0
#             else:
#                 return money[i]
#
#         # 이미 계산 된 값을 활용
#         ret = memo[i]
#         if ret != -1:
#             return ret
#
#         # 이 집을 털 경우
#         ret = DP(i + 2) + money[i]
#         # 이 집을 안 털 경우
#         ret = max(ret, DP(i + 1))
#         memo[i] = ret
#
#         return ret
#
#     answer_1 = DP(2) + money[0]
#     first_home = False
#     memo = [-1 for x in range(len(money))]
#     answer_2 = DP(1)
#
#     return max(answer_1, answer_2)


# DP 방식으로 풀지 않았을 때
# 테스트 코드는 다 맞지만 제출하면 전부 실패
#
# def solution(money):
#     answer = 0
#     # 돈이 큰 순서대로 정렬, i는 집번호
#     homes = [(i, v) for i, v in enumerate(money)]
#     homes.sort(key=lambda x: x[1], reverse=True)
#     # 털 수 없는 집은 1로 기억해두기
#     memo = [0 for i in range(len(money))]
#
#     # 돈이 제일 많은 집부터 순서대로 탐방하며 인접한 집은 memo=1로 변경하기
#     for home in homes:
#         if memo[home[0]] == 0:
#             # print(home)
#             answer += home[1]
#             memo[home[0]] = 1
#             if len(memo) != 1:
#                 memo[home[0] - 1] = 1
#                 if home[0] + 1 < len(memo):
#                     memo[home[0] + 1] = 1
#                 else:
#                     memo[0] = 1
#
#     temp = answer
#     answer = 0
#     memo = [0 for i in range(len(money))]
#
#     # 제일 돈 많은집은 못 턴다고 가정했을 때
#     for i, home in enumerate(homes):
#         if i != 0:
#             if memo[home[0]] == 0:
#                 # print(home)
#                 answer += home[1]
#                 memo[home[0]] = 1
#                 if len(memo) != 1:
#                     memo[home[0] - 1] = 1
#                     if home[0] + 1 < len(memo):
#                         memo[home[0] + 1] = 1
#                     else:
#                         memo[0] = 1
#         else:
#             memo[home[0]] = 1
#
#     return max(temp, answer)