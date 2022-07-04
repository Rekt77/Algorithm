import sys
import heapq
N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
INF = sys.maxsize
adj = [[] for _ in range(N+1)]
dp = [INF]*(N+1)

for _ in range(M):
    start, end, weight = map(int,sys.stdin.readline().strip().split())
    adj[start].append((weight,end))

src, tar = map(int,sys.stdin.readline().strip().split())

priorityQ = []
dp[src] = 0
heapq.heappush(priorityQ,(0,src))

while priorityQ:
    curw, vertex = heapq.heappop(priorityQ)
    if dp[vertex] < curw:
        continue
    for adjw,adjv in adj[vertex]:
        stacked_w=curw+adjw
        if stacked_w < dp[adjv]:
            dp[adjv] = stacked_w
            heapq.heappush(priorityQ,(stacked_w,adjv))
print(dp[tar])