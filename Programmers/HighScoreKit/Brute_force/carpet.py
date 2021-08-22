def solution(brown, yellow):
    max_w, min_w = yellow + 2, 3

    for w in range(max_w, min_w - 1, -1):
        h = (yellow / (w - 2)) + 2
        if h.is_integer() and brown == 2 * (w + h - 2):
            return [w, h]
