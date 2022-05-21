from collections import deque
import sys
myQueue = deque()
size = 0
N = int(sys.stdin.readline())
for _ in range(N):
    cmdline = sys.stdin.readline().strip()
    try:
        if cmdline=="front":
            print(myQueue[0])
        elif cmdline=="back":
            print(myQueue[-1])
        elif cmdline=="size":
            print(size)    
        elif cmdline=="empty":
            if myQueue:
                print(0)
            else:
                print(1)
        elif cmdline=="pop":
            print(myQueue.popleft())
            size-=1

        elif cmdline.startswith("push"):
            size += 1
            myQueue.append(int(cmdline[5:]))
    except IndexError:
        print(-1)