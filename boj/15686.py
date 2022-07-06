import sys
from itertools import combinations
N, M = map(int,sys.stdin.readline().strip().split())
ch_xy = []
house = []
ch_distance = []
for i in range(N):
    street = list(map(int,sys.stdin.readline().strip().split()))
    for j in range(N):
        if street[j] == 2:
            ch_xy.append((i,j))
        elif street[j] == 1:
            house.append((i,j))
ans = sys.maxsize
for ch_lists in combinations(ch_xy,M):
    tmp_ans = 0
    for house_xy in house:
        tmp = sys.maxsize
        for each_ch in ch_lists:
            tmp = min(tmp,abs(house_xy[0]-each_ch[0])+abs(house_xy[1]-each_ch[1]))
        tmp_ans+=tmp
    ans = min(ans,tmp_ans)
print(ans)