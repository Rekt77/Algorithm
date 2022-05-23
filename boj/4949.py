import sys
compare = ["(",")","[","]"]
while True:
    stack = []
    sentence = sys.stdin.readline()
    if sentence.startswith("."):
        break
    for alpha in sentence:
        if alpha in compare:
            if not stack:
                stack.append(alpha)
            else :
                if (ord(stack[-1])-ord(alpha)) == -1 or (ord(stack[-1])-ord(alpha)) == -2:
                    stack.pop()
                else:
                    stack.append(alpha)
    ans = "no" if stack else "yes"
    print(ans)