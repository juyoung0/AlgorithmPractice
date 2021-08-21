def solution(name):
    # 오른쪽, 왼쪽 중 더 가까이 갈 수 있는 곳을 선택한다.
    # 바꿔야 할 것이 모두 없어졌다면 종료한다.
    # 맨 오른쪽에서 오른쪽으로는 이동할 수 없음 -> 이것땜에 삽질한 것 같다.
    # dir=1 오른쪽, dir=-1 왼쪽
    # A->B로 바꾸는 경우와 A->Z로 바꾸는 경우 중 빠른 것 선택 필요하다
    change = [min(ord(i) - ord("A"), ord("Z") - ord(i) + 1) for i in name]
    step = 0
    curr_idx = 0

    if sum(change) == 0:
        return 0

    while (True):
        # 알파벳 변경
        step += change[curr_idx]
        change[curr_idx] = 0

        if sum(change) == 0:
            return step

        # 아직 바꿔야 할 게 있다면 이동
        prev_step, next_step = 1, 1
        while change[curr_idx + next_step] == 0:
            next_step += 1
        while change[curr_idx - prev_step] == 0:
            prev_step += 1

        step += next_step if next_step <= prev_step else prev_step
        curr_idx += next_step if next_step <= prev_step else -prev_step

    return step

# 10, 11 케이스 실패한 코드임
# def solution(name):
#     # A가 없는 쪽으로 움직인다.
#     # 본인이 A이면 넘어간다.
#     # 한 개 남았고, 그게 시작점이거나 A면 종료한다.
#     # dir=1 오른쪽, dir=-1 왼쪽
#     # A->B로 바꾸는 경우와 A->Z로 바꾸는 경우 중 빠른 것 선택 필요
#     notA = [idx for idx, val in enumerate(name) if val != 'A']
#     step = 0
#     dir = int((name[-1]=='A')or(name[1]!='A'))
#     if dir == 0:
#         dir = -1

#     move = 0
#     for i in range(len(name)):
#         if name[i*dir] != 'A':
#             step += min(abs(ord(name[i*dir]) - ord("A")), 91 - ord(name[i*dir]))
#         if move != len(name)-1:
#             step += 1
#         else:
#             if  name[i*dir] == 'A':
#                 step -= 1
#         move += 1

#     answer = step
#     return answer