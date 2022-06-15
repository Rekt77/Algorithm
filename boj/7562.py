import sys
from collections import deque

N = int(sys.stdin.readline().strip())
movements = [(1,2),(-1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,1),(-2,-1)]
for _ in range(N):
    size = int(sys.stdin.readline().strip())
    startY, startX = map(int,sys.stdin.readline().strip().split())
    tarY, tarX = map(int,sys.stdin.readline().strip().split())
    visited = [[-1]*size for _ in range(size)]
    queue = deque()
    queue.append((startY,startX))
    visited[startY][startX] = 0
    while queue:
        curY, curX = queue.popleft()
        if (curY,curX) == (tarY,tarX):
            print(visited[curY][curX])
            break
        for vy,vx in movements:
            if 0<=curY+vy<size and 0<=curX+vx<size and visited[curY+vy][curX+vx] == -1:
                visited[curY+vy][curX+vx] = visited[curY][curX] + 1
                queue.append((curY+vy,curX+vx))