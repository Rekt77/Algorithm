from collections import deque
import sys
sys.setrecursionlimit(10**6)
nCase = int(sys.stdin.readline())
vectors = [(0,1),(1,0),(0,-1),(-1,0)]

def dfs(x,y,earth):
    earth[y][x] = 2
    for v in vectors:
        if (0<=y+v[0]<len(earth)) and (0<=x+v[1]<len(earth[0])) and earth[y+v[0]][x+v[1]] == 1:
            dfs(x+v[1],y+v[0],earth)

for _ in range(nCase):
    counter = 0
    M,N,nCabage = map(int,sys.stdin.readline().strip().split())
    earth = [[0]*M for _ in range(N)]
    cabQueue = deque()
    for _ in range(nCabage):
        x,y = map(int,sys.stdin.readline().strip().split())
        earth[y][x] = 1
        cabQueue.append([x,y])
#queue를 이터레이팅 해서 dfs에 인자로 넣기
#if earth[y][x]가 이미 2이면 pass
    for i in range(nCabage):
        x,y = cabQueue.popleft()
        if earth[y][x] == 1:
            counter += 1
            dfs(x,y,earth)
    print(counter)
