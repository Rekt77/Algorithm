import sys
from collections import deque
N,M = map(int,sys.stdin.readline().strip().split())
board = [list(map(int,list(sys.stdin.readline().strip()))) for _ in range(N)]
queue = deque()
queue.append((0,0))
visited = [[False]*M for _ in range(N)]
visited[0][0] = True
while queue:
    curY,curX = queue.popleft()
    for vy,vx in [(0,1),(1,0),(-1,0),(0,-1)]:
        if 0<=curY+vy<N and 0<=curX+vx<M and board[curY+vy][curX+vx] != 0 and visited[curY+vy][curX+vx]==False:
            board[curY+vy][curX+vx] = board[curY][curX] + 1
            visited[curY+vy][curX+vx] = True
            queue.append((curY+vy,curX+vx))

print(board[N-1][M-1])
    