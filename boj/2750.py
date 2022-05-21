import heapq
N = int(input())
minheap = list()
for _ in range(N):
    heapq.heappush(minheap,int(input()))

for _ in range(N):
    print(heapq.heappop(minheap))