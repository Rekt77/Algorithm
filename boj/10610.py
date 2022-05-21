#Author Rekt77
import sys

N = sys.stdin.readline()[:-1]
numStr = sorted(N,reverse=True)
if not '0' in numStr:
    print(-1)
elif sum(map(int,numStr))%3==0:
    print("".join(numStr))
else:
    print(-1)