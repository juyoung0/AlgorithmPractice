# 입실을 먼저하고, 퇴실을 지금 할 수 있는 사람이 있는지 본다
# 퇴실 할 수 있는 사람이 없다면, 다음 사람을 입실시킨다
# 새로운 사람을 입실 시킬 때 마주치는 인원을 구한다

def solution(enter, leave):
    n = len(enter)
    meet = [set() for _ in range(n)]
    room = set()

    for e in enter:
        room.add(e)
        for r in room:
            meet[r-1].update(room - {r})

        while leave and leave[0] in room:
            room.remove(leave.pop(0))

    return [len(x) for x in meet]

print(solution([1, 4, 2, 3], [2, 1, 3, 4]), [2, 2, 1, 3])