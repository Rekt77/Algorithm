import sys

org = sys.stdin.readline().strip()
explode = sys.stdin.readline().strip()
stack = []
for each in org:
    stack.append(each)
    if explode[-1] == each and explode == "".join(stack[-len(explode):]):
        for _ in range(len(explode)):
            stack.pop()

print( "".join(stack) if stack else "FRULA")