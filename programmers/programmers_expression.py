from itertools import permutations

def solution(expression):
    answer = 0
    priorities = list(permutations(["+","*","-"]))

    for priority in priorities:
        last = []
        first = expression.split(priority[0])
        for partition in first:
            second = partition.split(priority[1])
            second = [str(eval(each)) for each in second]
            last.append(priority[1].join(second))
        last  = [str(eval(each)) for each in last]
        result=abs(eval(priority[0].join(last)))
        
        if result>answer:
            answer=result

    return answer

print(solution("50*6-3*2"))