n = int(input())

for i in range(n):
    scores = []
    ox = list(input())
    score = 0
    for answer in ox:
        if answer == 'O':
            score += 1
        else:
            score = 0

        scores.append(score)
    print(scores)
