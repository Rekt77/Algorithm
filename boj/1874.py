import sys

n = int(sys.stdin.readline())
numbers = []
stack = []
ans = []
for i in range(1,n+1):
    numbers.append(int(sys.stdin.readline()))
    stack.append(i)
    if numbers[0]<stack[-1]:
        print("NO")
        exit()
    ans.append("+")
    while stack and numbers[0]==stack[-1]:
        stack.pop()
        ans.append("-")
        numbers = numbers[1:]

print("\n".join(ans))