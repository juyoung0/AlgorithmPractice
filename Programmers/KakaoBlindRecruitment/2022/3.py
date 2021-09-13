import math

def solution(fees, records):
    answer = []
    info = {}
    for r in records:
        log = r.split(' ')
        if log[1] not in info:
            info[log[1]] = {'IN':-1, 'TIME':0}

        if log[2] == 'IN':
            info[log[1]]['IN'] = int(log[0][:2])*60 + int(log[0][3:])
        else:
            info[log[1]]['TIME'] += (int(log[0][:2])*60 + int(log[0][3:])) - info[log[1]]['IN']
            info[log[1]]['IN'] = -1

    for key in info.keys():
        if info[key]['IN'] != -1:
            info[key]['TIME'] += (23*60 + 59) - info[key]['IN']

    cars = list(info.keys())
    cars.sort()
    for car in cars:
        time = info[car]['TIME'] - fees[0]
        if time<0: time = 0
        fee = fees[1] + math.ceil((time / fees[2])) * fees[3]
        answer.append(fee)
    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]), [14600, 34400, 5000])