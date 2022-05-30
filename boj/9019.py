import sys
from collections import deque

N = int(sys.stdin.readline())
numbers = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(N) ]

DSLR = {"D":lambda x : (2*x)%10000,
        "S":lambda x : (x-1)%10000,
        "L":lambda x : (x%1000*10)+(x//1000),
        "R":lambda x : (x%10)*1000+(x//10)}

for number in numbers:
    cur, end = number
    visited = [False]*10001
    queue = deque([['', cur]])
    visited[cur] = True
    while queue:
        cmd, cur = queue.popleft()
        if cur==end:
            print(cmd)
            break
        for key in DSLR.keys():
            comp = DSLR[key](cur)
            if not visited[comp]:
                visited[comp] = True
                queue.append([cmd+key,comp])