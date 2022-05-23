import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque([ i for i in range(1,n+1)])

while True:
    if len(queue) == 1:
        print(queue[0])
        break
    queue.popleft()
    queue.append(queue.popleft())