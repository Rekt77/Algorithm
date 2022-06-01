from collections import deque
import sys

stair,snake = map(int,sys.stdin.readline().strip().split())
stairs = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(stair)]
snakes = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(snake)]
board = [0]*101
visited = [False]*101
for x,y in stairs:
    board[x] = y
for x,y in snakes:
    board[x] = y

queue = deque([1])
visited[1] = 0
while queue:
    cur = queue.popleft()
    for i in range(1,7):
        next_cur = cur+i
        if next_cur<=100:
            if board[next_cur]>0:
                next_cur = board[next_cur]
            if visited[next_cur]==False:
                visited[next_cur] = visited[cur]+1
                queue.append(next_cur)

print(visited[100])