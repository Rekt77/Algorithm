N, X = map(int,input().split())

A = [ int(num) for num in input().split()]
ans = []

for each in A:
    if X>each:
        ans.append(each)

print(*ans)