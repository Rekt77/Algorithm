import sys
import copy
from collections import deque

N = int(sys.stdin.readline().strip())
board = [[0]*N for _ in range(N)]
ans = 0

def setQ(y,x,tmp_board):
    tmp_board[y] = [1]*N
    for i in range(N):
        tmp_board[i][x] = 1
        if x-abs(y-i)>=0:
            tmp_board[i][x-abs(y-i)] = 1
        if x+abs(y-i)<N:
            tmp_board[i][x+abs(y-i)] = 1
    return copy.deepcopy(tmp_board)

def dfs(y,tmp_board):
    global ans

    if y==N-1:
        return 1

    for i in range(N):
        if sum(board[y+1]) == N:
                continue
        if tmp_board[y+1][i] == 0:
            if y+1 == (N-1):
                ans+=1
                continue
            board = setQ(y+1,i,copy.deepcopy(tmp_board))
            
            dfs(y+1,copy.deepcopy(board))

for i in range(N):
    board = [[0]*N for _ in range(N)]
    dfs(0,setQ(0,i,copy.deepcopy(board)))

print(ans)