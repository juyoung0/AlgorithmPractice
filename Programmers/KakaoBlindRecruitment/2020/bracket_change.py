# 210828 : 문제에 나온 수도코드로 안하고 직접하니 25분 -> 테스트 실패
# 수도코드 따라 재귀로 구현 28분 -> 테스트 성공
# 스택을 사용하여 balanced 인지 아닌지를 판별함

def make_right(w):
    stack = []
    v = ''
    u = ''
    reverse = False
    # step 1
    if len(w) == 0: return w

    # step 2
    for i, elem in enumerate(w):
        if len(stack) == 0:
            stack.append(elem)
        else:
            if stack[-1] == elem:
                stack.append(elem)
            else:
                # check ')' < '(' => True
                if stack[-1] > elem:
                    reverse = True
                stack.pop()

                if len(stack) == 0:
                    u = w[0:i+1]
                    v = w[i+1:]
                    break

    # step 3
    if not reverse:
        answer = u + make_right(v)
    # step 4
    else:
        answer = '(' + make_right(v) + ')'
        u = u[1:-1]
        for _u in u:
            if _u == '(':
                answer += ')'
            else:
                answer += '('

    return answer


# 문제대로 안 하고 직접 해결하려함 : 26분
def solution(p):
    answer = ''
    answer = make_right(p)

    return answer

solution("(()())()")
solution("()))((()")


# 다른 사람의 풀이
# def solution(p):
#     if p=='': return p
#     r=True; c=0
#     for i in range(len(p)):
#         if p[i]=='(': c-=1
#         else: c+=1
#         if c>0: r=False
#         if c==0:
#             if r:
#                 return p[:i+1]+solution(p[i+1:])
#             else:
#                 return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))
