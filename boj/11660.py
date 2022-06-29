import sys

N, M = map(int,sys.stdin.readline().strip().split())

board = [[0]*N for _ in range(N)]
stacked = [[0]*N for _ in range(N)]
tar_xy = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(M)]

for i in range(N):
    numbers = sys.stdin.readline().strip().split()
    for j in range(N):
        board[i][j] = int(numbers[j])
        if 0<i<N and 0<j<N:
            stacked[i][j] = stacked[i][j-1]+stacked[i-1][j]-stacked[i-1][j-1]+board[i][j]
        elif i==0:
            stacked[i][j] = stacked[i][j-1]+board[i][j]
        elif j==0:
            stacked[i][j] = stacked[i-1][j]+board[i][j]
        else:
            stacked[i][j] = board[i][j]


print(board)
print(stacked)