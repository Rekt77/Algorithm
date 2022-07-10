import sys
from collections import deque
N = int(sys.stdin.readline().strip())

house = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
init = [(0,0),(0,1),0]
vectors = [
    [((0,1),(0,1),0),((0,1),(1,1),1)],
    [((1,1),(0,1),0),((1,1),(1,0),2),((1,1),(1,1),1)],
    [((1,0),(1,0),2),((1,0),(1,1),1)]]

def RotandGo(yx):
    queue = deque()
    queue.append(yx)
    ans = 0
    while queue:
        pipe = queue.pop()
        vector = vectors[pipe[2]]

        if pipe[1][0] == (N-1):
            if pipe[2] == 2:
                continue

        if pipe[1][1] == (N-1) :
            if pipe[2] == 0:
                continue

        for xys in vector:
            nY=pipe[1][0]+xys[1][0]
            nX=pipe[1][1]+xys[1][1]

            if 0>nY or nY>=N or 0>nX or nX>=N:
                continue

            if house[nY][nX] == 1:
                continue

            #대각선일 때
            if xys[2] == 1:
                if house[nY][nX-1] == 1 or house[nY-1][nX] == 1:
                    continue

            if nY == (N-1) and nX == (N-1):
                ans +=1
                continue
            else:
                queue.append([
                    (pipe[0][0]+xys[0][0],pipe[0][1]+xys[0][1]),
                    (nY,nX), xys[2]])
        
    return ans
#print(RotandGo(init))

if house[N-1][N-1] != 1:
    print(RotandGo(init))
else:
    print(0)