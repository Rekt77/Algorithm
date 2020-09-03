def solution(progresses, speeds):
    point = 0
    count = 0
    answer=[]
    while point<len(progresses):
        if progresses[point]>=100:
            for i in range(point,len(progresses)):
                if progresses[i]>=100:
                    point +=1
                    count +=1
                else:
                    break
            answer.append(count)
        else:
            for i in range(point,len(progresses)):
                progresses[i]+=speeds[i]
            count = 0
    return answer

print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))