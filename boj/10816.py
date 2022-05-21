import sys
#-1천만~0 : 0~1천만
# 1 부터~ 1천만 : 1천만 1~2천만 
counter = [0]*20000001
N = int(sys.stdin.readline())
N_list=sys.stdin.readline().strip().split()
M = int(sys.stdin.readline())
M_list=sys.stdin.readline().strip().split()
for i in range(N):
    if int(N_list[i])<=0:
        counter[-int(N_list[i])] += 1
    else:
        counter[int(N_list[i])+10000000] += 1
for i in range(M):
    ans = counter[-int(M_list[i])] if int(M_list[i])<=0 else counter[int(M_list[i])+10000000]
    print(ans,end=" ")