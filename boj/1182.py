import sys
from itertools import combinations
N, S = map(int,sys.stdin.readline().strip().split())
elements = list(map(int,sys.stdin.readline().strip().split()))
ans = 0

for i in range(1,N+1):
    for each in combinations(elements,i):
        if sum(each) == S:
            ans += 1
print(ans)
"""
for i in range(N):
    if elements[i]==S:
        ans+=1
    for j in range(i,N):
        right = j+1
        while right<N:
            if sum(elements[i:j+1],elements[right]) == S:
                    ans+=1
            right +=1
print(ans)
"""