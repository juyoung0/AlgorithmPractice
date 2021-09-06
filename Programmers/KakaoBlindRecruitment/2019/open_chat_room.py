# 210906: 10분 소요

def solution(record):
    nickname = {}
    result = []
    answer = []
    for r in record:
        msg = r.split(' ')
        if msg[1] not in nickname:
            nickname[msg[1]] = msg[2]
        if msg[0] == 'Enter':
            nickname[msg[1]] = msg[2]
            result.append([msg[1], 0])
        elif msg[0] == 'Leave':
            result.append([msg[1], 1])
        else:
            nickname[msg[1]] = msg[2]

    for r in result:
        if r[1] == 0:
            answer.append("{}님이 들어왔습니다.".format(nickname[r[0]]))
        else:
            answer.append("{}님이 나갔습니다.".format(nickname[r[0]]))
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]), ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."])