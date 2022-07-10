import sys
from collections import deque

src, trg = map(int,sys.stdin.readline().strip().split())
ans = []
def dfs(src,trg,ntry):
    if src==trg:
        ans.append(ntry+1)
        return
    if src>trg:
        return
    dfs(src*2,trg,ntry+1)
    dfs((src*10)+1,trg,ntry+1)

dfs(src,trg,0)
print(min(ans) if ans else -1)