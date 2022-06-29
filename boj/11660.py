import sys

N, M = map(int,sys.stdin.readline().strip().split())

board = [[0]*(N+1) for _ in range(N+1)]
stacked = [[0]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    numbers = [0]+sys.stdin.readline().strip().split()
    for j in range(1,N+1):
        board[i][j] = int(numbers[j])
        stacked[i][j] = stacked[i][j-1]+stacked[i-1][j]-stacked[i-1][j-1]+board[i][j]

tar_xy = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(M)]

for y1,x1,y2,x2 in tar_xy:

    print(stacked[y2][x2]-stacked[y1-1][x2]-stacked[y2][x1-1]+stacked[y1-1][x1-1])