import sys
import copy

sys.setrecursionlimit(10**4)
N = int(sys.stdin.readline().strip())
org_grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
area=[(0),(0)]

def dfs(x,y,symbol,grid):
    grid[y][x] = 0
    for v in [(0,1),(1,0),(0,-1),(-1,0)]:
        # 만약 try-except을 쓴다면,
        # y+v[0] 이 0+(-1)일 경우 -> grid[-1][x]가 발생하여 except으로 가지 않음.
        # 범위를 정확히 명시하는 것이 중요함.
        if 0<=x+v[1]<len(grid) and 0<=y+v[0]<len(grid) and symbol==grid[y+v[0]][x+v[1]]:
            grid = dfs(x+v[1],y+v[0],symbol,grid)
    return grid

def RGmerge(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == "G":
                grid[i][j] = "R"
    return grid

grid = copy.deepcopy(org_grid)
RGgrid = RGmerge(copy.deepcopy(org_grid))

for i in range(N):
    for j in range(N):
        if grid[i][j] != 0:
            grid = dfs(j,i,grid[i][j],grid)
            area[0]+=1

        if RGgrid[i][j] != 0:
            RG_grid = dfs(j,i,RGgrid[i][j],RGgrid)
            area[1]+=1

print(area[0],area[1])