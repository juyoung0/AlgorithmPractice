# 명함 지갑 크기

def solution(sizes):
    sorted_sizes = [[max(s), min(s)] for s in sizes]
    size = list(zip(*sorted_sizes))
    return max(size[0]) * max(size[1])

# 다른 풀이
#    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
