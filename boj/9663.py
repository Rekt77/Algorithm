import sys

N = int(sys.stdin.readline().strip())
board = [0]*N
ans = 0

def avCheck(y):
    for i in range(y):
        if board[y] == board[i] or abs(y-i) == abs(board[y]-board[i]):
            return False
    return True

def setQ(y):
    global ans
    if y == N:
        ans += 1
        return 1
    else:
        for i in range(N):
            board[y] = i
            if avCheck(y):
                setQ(y+1)

setQ(0)
print(ans)
