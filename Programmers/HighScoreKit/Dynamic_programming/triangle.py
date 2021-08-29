# 210829 : 14분 memoization

def solution(triangle):
    sums = [triangle[-1]]

    for i in range(len(triangle) - 1, 0, -1):
        t_t = triangle[i - 1]
        b_t = sums[-1]
        temp = []
        for j, t_elem in enumerate(t_t):
            temp.append(max(t_elem + b_t[j], t_elem + b_t[j + 1]))
        sums.append(temp)

    return sums[-1][0]