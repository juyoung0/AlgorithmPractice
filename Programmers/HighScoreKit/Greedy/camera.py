def solution(routes):
    answer = 0
    # 진입지점이 낮은 것부터 정렬
    routes.sort(key=lambda x: x[0])
    
    # 차례대로 순회하며 나간 지점이 제일 낮은 곳을 기억하기 (제일 빨리 빠져나가는 차)
    # 다음 차량이 진입한 지점이 기억한 지점보다 높으면, 기억한 지점에 카메라 설치하기
    candi = 30001
    for route in routes:
        if route[0] > candi:
            answer += 1
            candi = 30001
        if route[1] < candi:
            candi = route[1]

    answer += 1
    return answer
