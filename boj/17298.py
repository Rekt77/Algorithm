import sys
n = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))
answer = [0 for _ in range(n)]
stack = []
for i in range(n):
    while True:
        if stack and numbers[stack[-1]] < numbers[i]:
            idx = stack.pop()
            answer[idx] = numbers[i]
        else :
            stack.append(i)
            break

while stack:
    idx = stack.pop()
    answer[idx] = -1
print(*answer)