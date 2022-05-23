import sys

n = int(sys.stdin.readline())

stack = []
for i in range(n):
    res = sys.stdin.readline().split()
    each_line = res[0]
    if each_line.startswith("push"):
        stack.append(int(res[1]))
        continue
    elif each_line.startswith("pop"):
        prt = stack.pop() if stack else -1 
    elif each_line.startswith("size"):
        prt = len(stack)
    elif each_line.startswith("empty"):
        prt = 0 if stack else 1
    elif each_line.startswith("top"):
        prt = stack[-1] if stack else -1
    print(prt)