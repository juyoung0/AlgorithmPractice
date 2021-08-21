# def solution(phone_book):
#     dict = {}

#     # 자릿수에 맞는 사전 만들면서 기존 사전과 비교해보기
#     for phone in phone_book:

#         # 이 단어가 누군가의 접두어일까?
#         if len(phone) in dict:
#             if phone in dict[len(phone)]:
#                 return False

#         # 이 단어의 접두어가 단어 전체인 단어가 있을까? & 사전 만들기
#         for i in range(len(phone)):
#             if i+1 in dict:
#                 if phone[:i+1] in dict[i+1]:
#                     return False
#                 elif phone[:i+1] not in dict[i+1]:
#                     dict[i+1].append(phone[:i+1])
#             else:
#                 dict[i+1] = []
#                 dict[i+1].append(phone[:i+1])

#     answer = True
#     return True

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True