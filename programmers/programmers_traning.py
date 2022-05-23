def solution(n, lost, reserve):
    new_reserve = set(reserve)-set(lost)
    new_lost = set(lost)-set(reserve)
    for student in new_lost:
        if student-1 in new_reserve:
            new_lost.remove(student-1)
        elif student+1 in new_reserve:
            new_lost.remove(student+1)
        else:
            n-=1
    return n

solution(5,[2,4],[1,3,5])