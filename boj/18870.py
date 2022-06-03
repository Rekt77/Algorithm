import heapq
import sys

N = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().strip().split()))
answer = [0]*N
heap = []

for i in range(N):
    heapq.heappush(heap,(numbers[i],i))

number,idx=heapq.heappop(heap)
tmp = number
cur = 0
answer[idx] = cur

while heap:
    number,idx=heapq.heappop(heap)
    if tmp == number:
        answer[idx] = cur
    else:
        tmp = number
        cur+=1
        answer[idx] = cur
    
print(*answer)