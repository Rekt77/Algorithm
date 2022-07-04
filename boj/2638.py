import sys
from collections import deque
N,M = map(int,sys.stdin.readline().strip().split())
board=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
counter = [[0]*M for _ in range(N)]

vX = (-1,0,1,0)
vY = (0,-1,0,1)
day = 0

queue1, queue2 = deque([(0,0)]),deque()
def check():
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                return False
    return True

def dayPassed():
    while queue1:
        y,x = queue1.popleft()
        for i in range(4):
            if 0<=y+vY[i]<N and 0<=x+vX[i]<M and not visited[y+vY[i]][x+vX[i]]:
                if board[y+vY[i]][x+vX[i]] == 1:
                    counter[y+vY[i]][x+vX[i]] += 1
                    if counter[y+vY[i]][x+vX[i]] == 2:
                        board[y+vY[i]][x+vX[i]] = 0
                        queue2.append((y+vY[i],x+vX[i]))
                        visited[y+vY[i]][x+vX[i]] = True
                else :
                    queue1.append((y+vY[i],x+vX[i]))
                    visited[y+vY[i]][x+vX[i]] = True

while True:
    dayPassed()
    day+=1
    if check():
        print(day)
        break
    queue1,queue2 = queue2,deque()
