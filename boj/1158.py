import sys
from collections import deque
N, K = list(map(int,sys.stdin.readline().split()))
people = deque([ i for i in range(1,N+1)])
ans = list()
while people:
    people.rotate(-(K-1))
    ans.append(str(people.popleft()))
print("<"+", ".join(ans)+">")