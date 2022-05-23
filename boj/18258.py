import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque()
cnt = 0
for _ in range(n):
    cmd = sys.stdin.readline()
    if cmd.startswith("push"):
        queue.append(int(cmd.split()[1]))
        cnt += 1
        continue
    elif cmd.startswith("pop"):
        if cnt:
            answer = queue.popleft()
            cnt -= 1
        else :
            answer = -1
    elif cmd.startswith("size"):    
        answer = cnt
    elif cmd.startswith("empty"):
        answer = 0 if cnt else 1
    elif cmd.startswith("front"):
        answer = queue[0] if cnt else -1
    elif cmd.startswith("back"):
        answer = queue[-1] if cnt else -1
    print(answer)