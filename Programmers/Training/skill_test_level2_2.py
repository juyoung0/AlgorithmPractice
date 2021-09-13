import math

def solution(progresses, speeds):
    answer = []
    days = []
    for i, p in enumerate(progresses):
        days.append(math.ceil((100 - p) / speeds[i]))

    jobs = 0
    prev_d = days[0]
    for d in days:
        if prev_d >= d:
            jobs += 1
        else:
            answer.append(jobs)
            jobs = 1
            prev_d = d
    answer.append(jobs)
    return answer