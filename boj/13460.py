import sys
H, W = map(int,sys.stdin.readline().strip().split())
board = [list(sys.stdin.readline().strip()) for _ in range(H)]
# if 구슬이 붙어있다면, 앞쪽에 있는 구슬 부터 이동
# 0이 벽과 만나는 지점에서만 골인 가능
def search_RB_EDGE(board):
    EDGES = []
    for i in range(1,len(board)-1):
        for j in range(1,len(board[0])-1):
            if board[i][j] == "R":
                R=(i,j)
            if board[i][j] == "B":
                B=(i,j)
            if board[i][j] == ".":
                if board[i-1][j] == "#" and board[i][j+1] == "#":
                    EDGES.append((i,j))
                elif board[i+1][j] == "#" and board[i][j+1] == "#":
                    EDGES.append((i,j))
                elif board[i-1][j] == "#" and board[i][j-1] == "#":
                    EDGES.append((i,j))
                elif board[i+1][j] == "#" and board[i][j-1] == "#":
                    EDGES.append((i,j))
    return R,B,EDGES

print(search_RB_EDGE(board))