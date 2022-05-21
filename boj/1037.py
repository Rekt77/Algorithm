import sys
import heapq

N = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().strip().split()))
heapq.heapify(numbers)

ans = numbers[0]*numbers[N-1]
print(ans)