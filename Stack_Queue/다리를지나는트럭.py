from collections import deque

def solution(bridge_length, weight, truck_weights):    
    b_truck = 0 # 현재 다리에 있는 트럭 수
    b_weight = 0 # 현재 다리에 있는 무게
    now = 1 # 현재 시간
    
    # 첫 번째 트럭 입장
    q = deque([(truck_weights[0], 1, now)])
    
    b_truck += 1
    b_weight += truck_weights[0]
    truck_weights = truck_weights[1:]

    while q :
        print(q)
        w, d, t = q.popleft()
        if t > now : # 다음 초
            now += 1
            # 새 트럭이 들어올 수 있는지 체크
            if truck_weights and b_truck < bridge_length and b_weight + truck_weights[0] < weight :
                q.append((truck_weights[0], 1, now))
                b_truck += 1
                b_weight += truck_weights[0]
                truck_weights = truck_weights[1:]

        if d + 1 > bridge_length : # 다리를 다 건넜으면
            b_weight -= w
            b_truck -= 1
        else : 
            q.append((w, d+1, t+1))

    return now


print(solution(2, 10, [7, 4, 5, 6]))