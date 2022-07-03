import sys
from collections import deque

def check():
    while auth_q1:
        y, x = auth_q1.popleft()
        if (y,x) == (tarY, tarX) :
            return True
        for vy, vx in [(0,1),(1,0),(0,-1),(-1,0)]:
            if 0<=y+vy<H and 0<=x+vx<W and not swan_visited[y+vy][x+vx]:
                if lake[y+vy][x+vx] == ".":
                    auth_q1.append((y+vy, x+vx))
                else :
                    auth_q2.append((y+vy, x+vx))
                swan_visited[y+vy][x+vx] = True
    return False

def dayPassed():
    while queue1:
        y, x = queue1.popleft()
        lake[y][x] = "."
        for vy, vx in [(0,1),(1,0),(0,-1),(-1,0)]:
            if 0<=y+vy<H and 0<=x+vx<W and not ice_visited[y+vy][x+vx]:
                if lake[y+vy][x+vx] == ".":
                    queue1.append((y+vy, x+vx))
                else :
                    queue2.append((y+vy,x+vx))
                ice_visited[y+vy][x+vx] = True

H, W = map(int,sys.stdin.readline().strip().split())
lake = [list(sys.stdin.readline().strip()) for _ in range(H)]
queue1,queue2 = deque(),deque()
auth_q1,auth_q2 = deque(),deque()
ice_visited = [[False]*W for _ in range(H)]
swan_visited = [[False]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if lake[i][j] == "L":
            if not auth_q1:
                auth_q1.append((i,j))
                swan_visited[i][j] = True
            else :
                tarY, tarX = i, j
            lake[i][j] = '.'

        if lake[i][j] == ".":
            queue1.append((i,j))
            ice_visited[i][j] = True
day = 0
while True:
    dayPassed()
    if check():
        print(day)
        break
    day+=1
    auth_q1,auth_q2 = auth_q2,deque()
    queue1,queue2 = queue2,deque()
