def solution(v):
    LT = [min([v[i][0] for i in range(3)]),max([v[i][1] for i in range(3)])]
    RT = [max([v[i][0] for i in range(3)]),max([v[i][1] for i in range(3)])]
    LB = [min([v[i][0] for i in range(3)]),min([v[i][1] for i in range(3)])]
    RB = [max([v[i][0] for i in range(3)]),min([v[i][1] for i in range(3)])]
    
    for each in [LT,RT,LB,RB]:
        if each not in v:
            return each

    
print(solution([[1, 1], [2, 2], [1, 2]]))