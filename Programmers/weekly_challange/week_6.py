# 복서 정렬하기
# 리스트 다중 sort key 는 튜플로 순서대로 묶기
# 애초에 sort() 함수는 동률일 경우 다음 요소를 보고 정렬한다고 한다

def solution(weights, head2head):
    answer = []
    infos = []  # win_ratio, win_w, weight, number
    for i, score in enumerate(head2head):
        win, lose, win_w = 0, 0, 0
        for j, s in enumerate(score):
            if s == 'W':
                win += 1
                if weights[i] < weights[j]:
                    win_w += 1
            elif s == 'L':
                lose += 1
            win_ratio = win / (win + lose) if win + lose != 0 else 0
        infos.append([win_ratio, win_w, weights[i], i + 1])

    infos.sort(key=lambda x: (-x[0], -x[1], -x[2], x[3]))
    return [x[3] for x in infos]
#   return list(zip(*infos))[3] 도 가능하다