import sys
from collections import deque
string = deque(sys.stdin.readline().strip())
tmp = deque()
N = int(sys.stdin.readline())

for _ in range(N):
    cmd = sys.stdin.readline().strip()
    if cmd.startswith("P"):
        string.append(cmd.split()[1])
    elif cmd == "L":
        if string:
            tmp.append(string.pop())
    elif cmd == "D":
        if tmp:
            string.append(tmp.pop())
    elif cmd == "B":
        if string:
            string.pop()
while tmp:
    string.append(tmp.pop())
    
print("".join(string))