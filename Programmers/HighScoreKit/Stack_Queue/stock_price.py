from collections import deque

def solution(prices):
    duration = [0] * len(prices)
    prices = enumerate(prices)
    stack = deque()
    time = 0
    process = []

    # 스택에 낮은수부터 넣고, 높은수가 나오면 pop 하기
    for p in prices:
        time += 1
        if stack:
            # 현재 가격이 스택에서 가장 높은 값보다 낮으면 -> 가격이 떨어진 것이다.
            while stack and p[1] < stack[-1][1]:
                duration[stack[-1][0]] = time - stack[-1][0] - 1
                process.append(stack[-1])
                stack.pop()
        stack.append(p)

    # 남은 스택 값들 처리
    time -= 1
    while stack:
        duration[stack[-1][0]] = time - stack[-1][0]
        process.append(stack[-1])
        stack.pop()

    answer = duration
    return answer