# 카카오 셔틀버스 문제

from collections import defaultdict
import datetime
from datetime import timedelta

def solution(n, t, m, timetable):
    bus = defaultdict(list)
    start = datetime.datetime(100, 1, 1, 9, 0, 0)
    delta = timedelta(minutes=t)
    for i in range(n):
        bus[str(start.hour).zfill(2) + str(start.minute).zfill(2)]
        start = start + delta

    timetable.sort()
    bus_time = sorted(list(bus.keys()))

    crew = 0
    for bt in bus_time:
        while len(bus[bt]) < m:
            if crew < len(timetable) and timetable[crew][:2] + timetable[crew][3:] <= bt:
                bus[bt].append(timetable[crew])
                crew += 1
            else:
                break
    # 제일 마지막 차 기준
    i = len(bus_time) - 1
    temp = bus_time[-1]
    while 0 <= i <= len(bus_time) and (len(bus[bus_time[i]]) == m):
        bus[bus_time[i]].sort()
        if temp >= bus[bus_time[i]][0][:2] + bus[bus_time[i]][0][3:]:
            if len(bus[bus_time[i-1]]) != m:
                first = datetime.datetime(100, 1, 1, int(bus[bus_time[i]][0][:2]), int(bus[bus_time[i]][0][3:]), 0)
                #delta = timedelta(minutes=1)
                answer = first # first - delta
                return "{}:{}".format(str(answer.hour).zfill(2), str(answer.minute).zfill(2))
            temp = bus[bus_time[i]][0]
            i -= 1
        else:
            print("there")

            first = datetime.datetime(100, 1, 1, int(temp[:2]), int(temp[2:]), 0)
            delta = timedelta(minutes=1)
            if bus[bus_time[i]][0] == bus[bus_time[i]][-1]:
                answer = first - delta
            else:
                answer = first
                if "{}:{}".format(str(answer.hour).zfill(2), str(answer.minute).zfill(2)) == bus[bus_time[i]][-1]:
                    answer = answer - delta
            return "{}:{}".format(str(answer.hour).zfill(2), str(answer.minute).zfill(2))
    else:
        if len(bus[bus_time[i]]) == m:
            bus[bus_time[i]].sort()
            first = datetime.datetime(100, 1, 1, int(bus[bus_time[i]][0][:2]), int(bus[bus_time[i]][0][3:]), 0)
            delta = timedelta(minutes=1)
            if bus[bus_time[i]][0] == bus[bus_time[i]][-1]:
                answer = first - delta
            else:
                answer = first
            return "{}:{}".format(str(answer.hour).zfill(2), str(answer.minute).zfill(2))
        else:
            return "{}:{}".format(bus_time[i][:2].zfill(2), bus_time[i][3:].zfill(2))

print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]), "09:00")
print(solution(1, 1, 1, ["23:59"]), "09:00")
print(solution(2, 1, 2,  ["09:00", "09:00", "09:00", "09:00"]), "08:59")
print(solution(2, 10, 2,["09:10", "09:09", "08:00"]), "09:09")
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]),"00:00")
print(solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]), "18:00")