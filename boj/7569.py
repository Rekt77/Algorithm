import sys
from collections import deque
def dayCalculator(pal):
    day = 0
    for i in range(len(pal)):
        for j in range(len(pal[0])):
            for k in range(len(pal[0][0])):
                if pal[i][j][k] == 0:
                    return -1
                day = max(day,max(pal[i][j]))
    return day-1

M, N, H= map(int,sys.stdin.readline().strip().split())
pallette = []
queue = deque()
for i in range(H):
    tmp = []
    for j in range(N):
        tmp.append(list(map(int,sys.stdin.readline().strip().split())))
        for k in range(M):
            if tmp[j][k] == 1:
                queue.append([i,j,k])
    pallette.append(tmp)

#위판, 아래판, 오른쪽, 아래쪽, 왼쪽, 위쪽
vector = [(1,0,0),(-1,0,0),(0,0,1),(0,1,0),(0,0,-1),(0,-1,0)]
while queue:
    i,j,k = queue.popleft()
    for vh,vy,vx in vector:
        if (0<=i+vh<H) and (0<=j+vy<N) and (0<=k+vx<M) and (pallette[i+vh][j+vy][k+vx] == 0):
            pallette[i+vh][j+vy][k+vx] = pallette[i][j][k]+1
            queue.append([i+vh,j+vy,k+vx])
print(dayCalculator(pallette))