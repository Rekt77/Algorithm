import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())

circle = deque([i for i in range(1,n+1)])
answer = ""
while circle :
    for _ in range(k-1):
        circle.append(circle.popleft())
    answer += str(circle.popleft())+", "
print("<"+answer[:-2]+">")