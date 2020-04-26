# Author Rekt77

import sys

def isSequence(list_):
    for i in range(1,len(list_)):
        list_[i-1] = list_[i]-list_[i-1]
    if min(list_[:-1]) == max(list_[:-1]):
        return True
    else:
        return False

N = int(sys.stdin.readline())
han = []
for i in range(101,N+1):
    if isSequence(list(map(int,list(str(i))))):
        han.append(i)
print(len(han)+99)