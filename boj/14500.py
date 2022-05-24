#python 3시간초과
#pypy3로만 동작
import sys

N,M = map(int,sys.stdin.readline().strip().split())
board = [ list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
tetromino = [
    [(0,0),(0,1),(0,2),(0,3)],
    [(0,0),(0,1),(1,1),(1,0)],
    [(0,0),(0,1),(0,2),(1,2)],
    [(0,0),(1,0),(1,1),(2,1)],
    [(0,0),(0,1),(0,2),(1,1)]
]# order : y,x

max_value = 0

# 대칭 : x값 부호변환
# 회전 : x,y스왑 후 x부호변환

for i in range(N):
    for j in range(M):
        for block in tetromino:
            for _ in range(2):
                block = list(map(lambda x: (x[0],-(x[1])),block))
                for _ in range(4):
                    block = list(map(lambda x: (x[1],-(x[0])),block))
                    if (0<=i+block[0][0]<N and 0<=j+block[0][1]<M) and (0<=i+block[1][0]<N and 0<=j+block[1][1]<M) and (0<=i+block[2][0]<N and 0<=j+block[2][1]<M) and (0<=i+block[3][0]<N and 0<=j+block[3][1]<M) :
                        max_value=max(
                            max_value,
                            board[i+block[0][0]][j+block[0][1]]+
                            board[i+block[1][0]][j+block[1][1]]+
                            board[i+block[2][0]][j+block[2][1]]+
                            board[i+block[3][0]][j+block[3][1]]
                            )
print(max_value)