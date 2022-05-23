#N=int(input())
#numbers = [ int(input()) for _ in range(N)]
#N = 7
#numbers = [1, 5, 2, 10, -99, 7, 5]
import sys
import heapq
input = sys.stdin.readline

n = int(input())
max_h, min_h = [], []

for i in range(n):
    num = int(input())
    if len(max_h) == len(min_h):
        heapq.heappush(max_h, -num)
    else:
        heapq.heappush(min_h, num)

    if len(max_h) >= 1 and len(min_h) >= 1 and -max_h[0] > min_h[0]:
        max_value = heapq.heappop(max_h)
        min_value = heapq.heappop(min_h)
        
        heapq.heappush(max_h, -min_value)
        heapq.heappush(min_h, -max_value)

    print(-max_h[0])