N = int(input())
parenthesis = [ input() for _ in range(N)]

for bundle in parenthesis:
    stack = []
    for each in bundle:
        try:
            if (stack[-1]+each)=="()":
                stack.pop()
            else:
                stack.append(each)
        except IndexError:
            stack.append(each)
    if stack:
        print("NO")
    else:
        print("YES")