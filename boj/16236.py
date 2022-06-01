# 구현은 되지만 무조건 시간초과 나오는 코드
import sys
from collections import deque
import heapq
import copy
N = int(sys.stdin.readline())
aquarium = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
sharkSize = 2

# 힙에 먹을 수 있는 물고기 좌표 다 넣는다
# ㄴ 좌표를 넣을 때 (거리,(tarY,tarX))
# 위에서 하나씩 꺼내고 갈 수 있는 지 체크
# 갈 수 있으면 sharkSize += 1, curLoc = (tarY,tarX)
def sharkAndtarget(shark,aq):
    target = []
    for i in range(len(aq)):
        for j in range(len(aq)):
            if aq[i][j] == 9:
                loc = (i,j)
            if aq[i][j] != 9 and 0<aq[i][j]<shark:
                target.append((i,j))
    return loc,target

#dfs
def distanceCheck(curX,curY,tarX,tarY,visited,sharkSize):
    if (tarX,tarY) == (curX,curY):
        return 1

    for vy,vx in [(0,1),(1,0),(0,-1),(-1,0)]:
        next_curX = curX+vx
        next_curY = curY+vy
        if 0<=next_curX<N and 0<=next_curY<N and (visited[next_curY][next_curX] == False or visited[next_curY][next_curX]>visited[curY][curX]+1):
            if aquarium[next_curY][next_curX] <= sharkSize:
                visited[next_curY][next_curX] = visited[curY][curX] + 1
                distanceCheck(next_curX,next_curY,tarX,tarY,visited,sharkSize)

    return visited[tarY][tarX]

visited = [[False]*N for _ in range(N)]

time = 0
counter = 0
cur, target =sharkAndtarget(sharkSize,aquarium)

while target:
    priority = []
    for i in range(len(target)):
        c_visited = copy.deepcopy(visited)
        c_visited[cur[0]][cur[1]] = 1
        distance = distanceCheck(cur[1],cur[0],target[i][1],target[i][0],c_visited,sharkSize)
        if distance:
            #거리 , y , x
            heapq.heappush(priority,(distance-1, target[i][0], target[i][1]))
    if not priority:
        break
    else :
        dead=heapq.heappop(priority)
        time += dead[0]
        #상어위치-물고기 위치 스왑
        aquarium[cur[0]][cur[1]] = 0
        aquarium[dead[1]][dead[2]] = 9
        counter += 1
        if counter==sharkSize:
            sharkSize+=1
            counter = 0
        cur, target = sharkAndtarget(sharkSize,aquarium)

#    for each in aquarium:
#        print(each)
    
#    print("")

print(time)