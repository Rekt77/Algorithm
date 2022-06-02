# 힙을 사용하는게 핵심
# (거리,y좌표, x좌표) 힙으로 정렬
# dfs로는 절대 풀리지 않음
# bfs로 풀시 먹을 수 있는 물고기가 같은 거리 2에 있을경우
# ㄴ 상어: (0,1) 물고기1: (1,0,0), 물고기2: (1,0,2) -> 물고기 1,2를 힙으로 정렬시 (1,0,0)이 앞에옴
#  ㄴ 물고기를 먹고 힙을 초기화, 거리 계산도 0으로 초기화하여 먹은 시점에서 부터 다른 물고기를 찾으러 bfs 하면 정답
import sys
from collections import deque
import heapq
import copy
N = int(sys.stdin.readline())
aquarium = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
sharkSize = 2

def sharkFinder(aq):
    for i in range(len(aq)):
        for j in range(len(aq)):
            if aq[i][j] == 9:
                loc = (i,j)
                aq[i][j] = 0
                return loc

visited = [[False]*N for _ in range(N)]
c_visited = copy.deepcopy(visited)
priority = []
time = 0
counter = 0
cur = sharkFinder(aquarium)
heapq.heappush(priority,(0,cur[0],cur[1]))

while priority: 
    distance, curY, curX = heapq.heappop(priority)
    c_visited[curY][curX] = True

    if 0<aquarium[curY][curX]<sharkSize:
        aquarium[curY][curX] = 0
        time += distance
        counter += 1

        if counter==sharkSize:
            sharkSize+=1
            counter = 0
        distance = 0
        priority = []
        c_visited = copy.deepcopy(visited)
        
    for vy,vx in [(0,1),(1,0),(0,-1),(-1,0)]:
        next_curX = curX+vx
        next_curY = curY+vy
        if 0<=next_curX<N and 0<=next_curY<N:
            if aquarium[next_curY][next_curX] <= sharkSize and c_visited[next_curY][next_curX] == False:
                c_visited[next_curY][next_curX] = True
                heapq.heappush(priority,(distance+1, next_curY, next_curX))

print(time)