def solution(bridge_length, weight, truck_weights):
    answer = bridge_length
    bridge=[0]*bridge_length
    while truck_weights:
        bridge.pop(0)
        answer+=1
        try:
            if sum(bridge)+truck_weights[0]<=weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
        except:
            pass
    return answer

solution(3,10,[5,5,5])