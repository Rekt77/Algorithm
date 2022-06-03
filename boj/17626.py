from re import A
import sys
from itertools import combinations

N = int(sys.stdin.readline())
i = 1
rainbow = [0]
while i**2<=N:
    rainbow.append(i**2)
    i+=1

for i in range(len(rainbow)):
    for j in range(len(rainbow)):
        for k in range(len(rainbow)):
            for l in range(len(rainbow)):
                if rainbow[i]+rainbow[j]+rainbow[k]+rainbow[l] == N:
                    print(4-[rainbow[i],rainbow[j],rainbow[k],rainbow[l]].count(0))
                    exit()