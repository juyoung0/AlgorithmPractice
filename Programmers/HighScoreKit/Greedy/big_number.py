def solution(number, k):
    answer = ''

    start_idx = 0

    # 같은 범위 내에서 최대값이 있다면 그 앞까지는 지워도 됨
    while k > 0 and start_idx + k <= len(number):
        if start_idx + k == len(number):
            return answer

        if number[start_idx] == "9":
            answer += number[start_idx]
            start_idx += 1
        else:
            for i in range(k):
                # 첫 수 보다 큰 수가 있는지 검사
                if number[start_idx] < number[start_idx + i + 1]:
                    k -= (i + 1)
                    start_idx = start_idx + i + 1
                    break;
                else:
                    # 첫 수가 가장 큰 수였을 때
                    if i == k-1:
                        answer += number[start_idx]
                        start_idx += 1

    answer += number[start_idx:]

    return answer


# 스택으로 풀기
# def solution(number, k):
#     st = []
#     for i in range(len(number)):
#         while st and k > 0 and st[-1] < number[i]:
#             st.pop()
#             k -= 1
#         st.append(number[i])
#     return ''.join(st[:len(st) - k])