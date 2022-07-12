import sys

nTest = int(sys.stdin.readline().strip())
def tear(i,j):
    for vy, vx in [(0,-1),(0,1),(1,0),(-1,0)]:
        if 0<=i+vy<2 and 0<=j+vx<len(stickers[0]):
            stickers[i+vy][j+vx] = 0

def itsValue(i,j):
    tmp = 0
    for vy, vx in [(0,-1),(0,1),(1,0),(-1,0)]:
        if 0<=i+vy<2 and 0<=j+vx<len(stickers[0]):
            tmp = max(tmp,stickers[i+vy][j+vx])
    return tmp

for _ in range(nTest):
    nCol = int(sys.stdin.readline().strip())
    stickers = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(2)]
    for i in range(2):
        for j in range(nCol):
            if itsValue(i,j) <= stickers[i][j]:
                tear(i,j)
    print(sum(stickers[0])+sum(stickers[1]))