# Sweepping algorithm, Segment Tree
# 전부 파티션 나누는 방법으로 했으나 시작/끝이 같은 시청에 대헛
# 구분을 할 수 없는 문제가 있어 다시 풀기로 함

from queue import PriorityQueue
import heapq

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
    # 모든 겹치는 구간을 나눈다 (시작점, 끝점, 겹치는 갯수)
    log_list = []
    heap = []
    play = time_parser(play_time)
    adv = time_parser(adv_time)
    if adv == play:
        return reverse_parser(0)

    viewer = [0 for _ in range(play)]
    print(time_parser(adv_time))

    # log를 활용 가능한 포맷으로 변경하기
    for log in logs:
        temp = log.split('-')
        log_list.append((time_parser(temp[0]), time_parser(temp[1])))
    log_list.sort()

    # 구간 나누기
    def seperate():
        div = []
        prev = 0
        log_cnt = 0
        for log in log_list:
            left, right = log[0], log[1]
            if len(heap) == 0:
                div.append((prev, left, log_cnt))
                prev = left
                heapq.heappush(heap, right)
                log_cnt += 1
                continue

            min_val = heap[0]
            # 다음 로그가 새로 겹쳐짐
            if min_val >= left:
                div.append((prev, left-1, log_cnt))
                prev = left
                heapq.heappush(heap, right)
                if min_val != left:
                    log_cnt += 1
            # 다음 로그가 겹쳐지기 전에 먼저 끝나는 구간이 있음
            else:
                while min_val < left:
                    if len(heap) != 0:
                        min_val = heapq.heappop(heap)
                    div.append((prev, min_val, log_cnt))
                    prev = min_val + 1
                    log_cnt -= 1
                    if len(heap) == 0:
                        min_val = left
                        break

                div.append((prev, min_val, log_cnt))
                prev = min_val + 1
                heapq.heappush(heap, right)
                log_cnt += 1

        # 남은 구간들 처리해주기
        if len(heap) != 0:
            min_val = heapq.heappop(heap)
            while len(heap) > 0:
                div.append((prev, min_val, log_cnt))
                prev = min_val + 1
                log_cnt -= 1
                if len(heap) != 0:
                    min_val = heapq.heappop(heap)

        div.append((prev, min_val, log_cnt))
        div.append((min_val, play, 0))

        return div

    div = seperate()

    print(log_list)
    print(div)

    for d in div:
        viewer[d[0]:d[1]+1] = [d[2]] * (d[1]+1-d[0])

    # 광고를 가장 많이 시청하는 구간을 찾는다
    max_time = 0
    views = sum(viewer[0:adv])
    max_view = views
    for i in range(1, play-adv):
        views = views - viewer[i-1] + viewer[i+adv]
        if max_view < views:
            max_time = i
            max_view = views

    return reverse_parser(max_time)

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]), "01:30:59")
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]), "00:00:00")
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]), "01:00:00")
print(solution("00:10:00", "00:05:00", ["00:05:00-00:10:00"]), "00:05:00")