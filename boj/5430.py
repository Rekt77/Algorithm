import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    flag = False
    cmdline = deque(sys.stdin.readline().rstrip())
    n = len(cmdline)
    lennum = int(sys.stdin.readline())
    try:
        numbers = deque(map(int,sys.stdin.readline().rstrip()[1:-1].split(",")))
    except:
        numbers = deque()
    while cmdline:
        cmd = cmdline.popleft()
        n-=1
        if cmd == "R":
            flag ^= True
        else :
            try:
                if flag:
                    numbers.pop()
                else :
                    numbers.popleft()
            except IndexError:
                print("error")
                break
        if n == 0:
            if flag:
                numbers.reverse()
            print("["+",".join(list(map(str,numbers)))+"]")
    