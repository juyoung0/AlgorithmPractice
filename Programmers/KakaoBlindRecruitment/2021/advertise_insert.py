def time_parser(time):
    sec = int(time[0:2]) * 3600
    sec += int(time[3:5]) * 60
    sec += int(time[6:8])
    return sec

def reverse_parser(time):
    sec = time % 60
    min = ((time - sec) % 3600)//60
    hour = (time - min) // 3600
    return "{}:{}:{}".format(str(hour).zfill(2), str(min).zfill(2), str(sec).zfill(2))

def solution(play_time, adv_time, logs):
    play = time_parser(play_time)
    adv = time_parser(adv_time)
    views = [0 for _ in range(play + 1)]

    if adv == play:
        return reverse_parser(0)

    # 시작, 끝 시점 기록해주기
    for log in logs:
        start, end = log.split('-')
        start = time_parser(start)
        end = time_parser(end)
        views[start] += 1
        views[end] -= 1

    # 각 초 마다의 view 수 구하기 (쭉 슬라이딩하며 밀어주기)
    for i in range(1, len(views)):
        views[i] = views[i] + views[i - 1]

    # 각 초가 되었을 때의 누적 view 값 구해주기
    for i in range(1, len(views)):       # 4
        views[i] = views[i] + views[i - 1]

    max_view = 0
    max_time = 0
    for i in range(adv - 1, play):
        if i >= adv:
            if max_view < views[i] - views[i - adv]:
                max_view = views[i] - views[i - adv]
                max_time = i - adv + 1
        else:
            if max_view < views[i]:
                max_view = views[i]
                max_time = i - adv + 1

    return reverse_parser(max_time)

# 다른 풀이 (내 첫 시도와 유사함)
# def solution(play, adv, logs):
#     c = lambda t: int(t[0:2]) * 3600 + int(t[3:5]) * 60 + int(t[6:8])
#     play, adv = c(play), c(adv)
#     logs = sorted([s for t in logs for s in [(c(t[:8]), 1), (c(t[9:]), 0)]])
#
#     v, p, b = 0, 0, [0] * play
#     for t, m in logs:
#         if v > 0:
#             b[p:t] = [v] * (t - p)
#         v, p = v + (1 if m else -1), t
#
#     mv, mi = (s := sum(b[:adv]), 0)
#     for i, j in zip(range(play - adv), range(adv, play)):
#         s += b[j] - b[i]
#         if s > mv:
#             mv, mi = s, i + 1
#
#     return f"{mi//3600:02d}:{mi%3600//60:02d}:{mi%60:02d}"

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]), "01:30:59")
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]), "00:00:00")
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]), "01:00:00")
print(solution("00:10:00", "00:05:00", ["00:05:00-00:10:00", "00:05:00-00:10:00"]), "00:05:00")
