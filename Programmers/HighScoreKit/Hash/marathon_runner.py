def solution(participant, completion):
    participant.sort()
    completion.sort()

    answer = ''

    for i in range(len(participant)):
        if i < len(completion):
            if participant[i] != completion[i]:
                answer = participant[i]
                break
        else:
            answer = participant[i]
    return answer