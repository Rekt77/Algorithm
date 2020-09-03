
string = "abaaba"
stack = []
if len(string)%2 != 0:
    print(0)
for each in string:
    stack.append(each)
    if len(stack) != 1 and (stack[-1]==stack[-2]):
        stack.pop()
        stack.pop()

print(stack)
if stack:
    print(0)
else:
    print(1)