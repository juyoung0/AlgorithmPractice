# dict = {}

# def findNext(j):
#     answer = ""
#     elem = dict[str(j)]
#     if len(elem) == 1:
#         answer += str(j)
#         dict[str(j)].remove(answer)
#         j -= 1
#     elif len(elem) == 0:
#         j -= 1
#     else:

#     # 한자리수가 있다면, 다음 작은 수와 조합하여 쓸 수 있는지 체크.
#     if elem[-1] < 10:
#         max_next = max(list(map(lambda x : x[idx], elem[:len(elem)-1])))
#         lower = j - 1
#         # j를 단독으로 붙이는 게 이득인지 확인
#         while(lower > max_next):
#             if len(dict[lower]) > 0:
#                 elem2 = dict[str(lower)]
#                 answer += str(j)
#                 answer += str(lower)
#                 dict[str(j)].remove(j)
#                 dict[str(lower)].remove(lower)
#                 break;
#             else:
#                 lower -= 1

#         if lower == max_next:
#     # 한자리수가 없다면 두자리 수 비교
#     else:
#         idx += 1

#     return answer

# def solution(numbers):
#     answer = ""
#     dict = {}
#     numbers = list( map(str, numbers) )
#     numbers.sort(key=str(x), reverse=True)

#     for i in range(10):
#         dict[str(i)] = []

#     for n in numbers:
#         dict[str(n)[0]].append(str(n))

#     j = 9
#     loc = 1
#     while(j < 0):
#             answer += findNext(j)

#     return numbers

def solution(numbers):
    # 0. key point
    numbers_str = [str(num) for num in numbers]  # 1. 사전 값으로 정렬하기
    numbers_str.sort(key=lambda num: num * 3, reverse=True)  # 2. number는 1000이하의 숫자이므로 x3(반복)한 값으로 비교

    return str(int(''.join(numbers_str)))