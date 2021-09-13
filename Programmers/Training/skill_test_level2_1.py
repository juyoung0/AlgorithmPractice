from collections import deque

def solution(s):
    stack = deque()
    if s.count('(') != s.count(')'):
        return False

    for _s in s:
        if _s == '(':
            stack.append(_s)
        else:
            if len(stack) == 0 or stack.pop() != '(':
                return False

    if len(stack) != 0: return False
    return True