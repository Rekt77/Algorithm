import heapq
import sys
maxheap = list()
minheap = list()
ans = 0
N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().strip().split()))
B = list(map(lambda x : -int(x),sys.stdin.readline().strip().split()))
heapq.heapify(A)
heapq.heapify(B)
for _ in range(N):
    ans += heapq.heappop(A)*(-heapq.heappop(B))
print(ans)