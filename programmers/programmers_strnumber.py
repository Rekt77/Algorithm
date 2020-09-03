def solution(s):
    MIN = min(map(int,s.split(" ")))
    MAX = max(map(int,s.split(" ")))
    answer = "%d %d"%(MIN,MAX)
    return answer