import sys
from collections import deque
N,M = map(int,sys.stdin.readline().strip().split())
farm = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(M)]
queue = deque()

def isDone(farm):
    Max = 0
    for i in range(len(farm)):
        for j in range(len(farm[0])):
            if farm[i][j] == 0:
                return False
            Max = max(Max,farm[i][j])
    return Max
    

for i in range(M):
    for j in range(N):
        if farm[i][j] == 1:
            queue.append((1,i,j))

while queue:
    val, tomY, tomX = queue.popleft()
    for vy,vx in [(0,1),(-1,0),(0,-1),(1,0)]:
        if 0<=tomX+vx<N and 0<=tomY+vy<M and farm[tomY+vy][tomX+vx] == 0 :
            farm[tomY+vy][tomX+vx] = val+1
            queue.append((val+1,tomY+vy,tomX+vx))

ans = isDone(farm)
print(ans-1 if ans else -1)