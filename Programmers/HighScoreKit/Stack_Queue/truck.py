from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque()
    truck = deque(truck_weights)
    time = 0
    bridge.append((time + bridge_length, truck.popleft()))
    total_weight = bridge[0][1]

    while True:
        time += 1

        # 다리에서 벗어나는 트럭이 있는 지 확인
        if bridge:
            if bridge[0][0] == time:
                total_weight -= bridge[0][1]
                bridge.popleft()
        else:
            break;

        if truck:
            # 다리에 새로운 트럭 진입
            if total_weight + truck[0] <= weight:
                total_weight += truck[0]
                bridge.append((time + bridge_length, truck.popleft()))

    answer = time

    return answer