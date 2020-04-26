#Author Rekt77
import sys

N = sys.stdin.readline()[:-1]
numStr = sorted(N,reverse=True)
if not '0' in numStr:
    print('-1')
if not sum(map(int,numStr))%3==0:
    print('-1')
else :
    print("".join(numStr))