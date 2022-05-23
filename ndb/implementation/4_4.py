import sys
H, W = map(int,sys.stdin.readline().strip().split())
init_c,init_r,locate = map(int,sys.stdin.readline().strip().split())
nesw=[(-1,0),(0,-1),(1,0),(0,1)]
board = [sys.stdin.readline().strip().split() for _ in range(H)]
board[init_r][init_c] = "1"
count,turn = 0, 0
#go
while True:
    #turn left
    locate+=1
    locate%=4
    if (0<=(init_r+nesw[locate][0])<H) and (0<=(init_c+nesw[locate][1])<W) and board[init_r+nesw[locate][0]][init_c+nesw[locate][1]] != "1" :
        init_c, init_r = init_c+nesw[locate][1], init_r+nesw[locate][0]
        board[init_r][init_c] = "1"
        count +=1
        turn = 0
        continue
    else:
        turn += 1
    
    if turn == 4:
        if (0<=init_r-nesw[locate][0]<H) and (0<=init_c-nesw[locate][1]<=W) and (board[init_r-nesw[locate][0]][init_c-nesw[locate][1]]) == "0":
            board[init_r-nesw[locate][0]][init_c-nesw[locate][1]] = "1"
            init_c, init_r = init_r-nesw[locate][0],init_c-nesw[locate][1]
            turn = 0
            count += 1
        else:
            break

