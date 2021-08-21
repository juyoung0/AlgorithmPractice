import math

def solution(citations):
    citations.sort(reverse=True)
    candi = list(x + 1 for x in range(len(citations)) if citations[x] >= x + 1)
    if len(candi) == 0:
        return 0
    else:
        return max(candi)

# 첫 번 째 시도
# def solution(citations):
#     answer = 0
#     citations.sort(reverse=True)
#     mid = math.ceil(len(citations)/2)
#     start, end = 0, len(citations)-1
#     if len(citations) == 1:
#         if citations[0] >= 1:
#             return 1
#         else:
#             return 0

#     while(True):
#         if citations[mid] >= mid+1:
#             if len(citations) - mid <= citations[mid]:
#                 answer = mid + 1
#                 break;
#             else:
#                 start = mid
#                 mid = math.ceil((end - start)/2)
#         else:
#                 end = mid
#                 mid = math.ceil((end - start)/2)

#     return answer