def solution(progresses, speeds):
    answer = []
    while progresses:
        count = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        #스택의 맨 위가 100이상인지 검사하고 100이 넘으면 pop 하는 반복문
        try:
            while progresses[0]>=100:
                progresses.pop(0)
                speeds.pop(0)
                count+=1
        except IndexError:
            pass

        if count > 0:
            answer.append(count)
    return answer

print(solution([93, 30, 55],[1, 30, 5]))