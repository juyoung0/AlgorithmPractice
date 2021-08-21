def solution(answers):
    scores = [0, 0, 0]
    rules = [[1, 2, 3, 4, 5],
             [2, 1, 2, 3, 2, 4, 2, 5],
             [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
             ]
    index = [0, 0, 0]
    result = []

    for answer in answers:
        for i in range(3):
            if index[i] >= len(rules[i]):
                index[i] = 0

            if answer == rules[i][index[i]]:
                scores[i] += 1
            index[i] += 1

    max_score = 0
    for i in range(3):
        if scores[i] >= max_score:
            max_score = scores[i]

    for i in range(3):
        if scores[i] == max_score:
            result.append(i + 1)

    return result