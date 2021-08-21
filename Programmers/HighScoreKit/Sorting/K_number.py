def solution(array, commands):
    answers = []
    for comm in commands:
        temp = array[comm[0] - 1:comm[1]]
        temp.sort()

        answers.append(temp[comm[2] - 1])
    return answers