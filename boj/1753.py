import heapq
import sys


Nvertex, Nedge = map(int,sys.stdin.readline().strip().split())
start = int(sys.stdin.readline().strip())
INF = sys.maxsize

visited = [False]*(Nvertex+1)
w_map = [INF]*(Nvertex+1)
w_map[start] = 0
adj = dict()

for _ in range(Nedge):
    Svertex, Tvertex, W = map(int,sys.stdin.readline().strip().split())
    if adj.get(Svertex):
        adj[Svertex].append((W,Tvertex))
    else :
        adj[Svertex] = [(W,Tvertex)]

bfs_queue = []
heapq.heappush(bfs_queue,(0,start))
while bfs_queue:
    curW,curV = heapq.heappop(bfs_queue)
    if not adj.get(curV):
        continue
    for adjW,adjV in adj[curV]:
        if w_map[adjV] > curW+adjW:
            heapq.heappush(bfs_queue,(curW+adjW,adjV))
            w_map[adjV] = curW+adjW

for i in range(1,len(w_map)):
    if w_map[i] == INF:
        print("INF")
    else:
        print(w_map[i])