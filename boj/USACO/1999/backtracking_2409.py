from itertools import combinations
M = int(input())
lpipes = [int(each) for each in input().split()]
N = int(input())
spipes = [int(each) for each in input().split()]

for i in range(M):
    for j in range(1,len(spipes)+1):
        min = lpipes[i]
        if len(spipes) == 0:
            break
        for each in combinations(spipes,j):
            if lpipes[i]>=sum(each):
                if lpipes[i]-sum(each)<=min:
                    min = lpipes[i]-sum(each)
                    tmp = each
                    if min==0:
                        break
    for n in tmp:
        spipes.remove(n)
    tmp = tuple()

print(N-len(spipes))