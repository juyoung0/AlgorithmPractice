def solution(n, weak, dist):
    gap = []  # [0 for _ in range(n)]
    # next_w = []#[0 for _ in range(n)]
    prev_weak = -1
    check = 0
    answer = 0

    # 각 weak 사이의 거리를 담은 배열을 만든다
    for w in weak:
        if prev_weak == -1:
            prev_weak = w
        else:
            gap.append([w - prev_weak, prev_weak, w])
            # next_w.append((prev_weak, w)#[prev_weak] = w
            prev_weak = w
    gap.append([weak[0] + n - weak[-1], weak[-1], weak[0]])
    # next_w((weak[-1], weak[0])
    dist.sort()
    #print(gap)
    # weak 사이의 간격이 가장 먼 weak 두 지점중 뒤 쪽 지점에서 시계 방향으로 회전한다
    # 가장 많이 움직일 수 있는 사람부터 움직인다
    while check < len(weak):
        curr_w = gap.index(max(gap, key=lambda x: x[0]))  # 5
        if len(dist) == 0:
            return False
        checker = dist[-1]
        dist = dist[:-1]
        del_list = []
        answer += 1

        # 점검 하며 지나친 weak 세며, gap 업데이트 해주기
        walk = gap[curr_w][2] + checker
        #walk = walk - n if walk >= n else walk
        #prev_w = len(gap) - 1 if curr_w == 0 else curr_w - 1
        next_w = 0 if curr_w == len(gap) - 1 else curr_w + 1
        gap[curr_w][0] += gap[next_w][0]
        gap[curr_w][2] = gap[next_w][2]
        prev_w = curr_w
        del_list.append(next_w)
        check += 1

        if gap[curr_w][1] == gap[curr_w][2]:
            break
        #print("curr_w : ", gap[curr_w], "walk : ", walk, " next_w : ", gap[next_w])
        while gap[next_w][2] <= walk:
            curr_w = next_w
            next_w = 0 if curr_w == len(gap) - 1 else curr_w + 1
            gap[prev_w][0] += gap[next_w][0]
            gap[prev_w][2] = gap[next_w][2]
            del_list.append(next_w)
            check += 1
            #print("walk : ", walk, " checker : ", checker, "prev_w : ", gap[prev_w], "curr_w : ", gap[curr_w], " next_w : ", gap[next_w] )

        #print(gap)
        #print(del_list)
        del gap[del_list[0]:del_list[-1]+1]
        #print(gap)
        #print("=====")
        # if len(gap) >= 1:
        #     answer += 1
        # else:
        #     return 0
    return answer

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]), 2)
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]), 1)