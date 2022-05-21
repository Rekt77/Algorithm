import sys

N = int(sys.stdin.readline())
N_list = list(map(int,sys.stdin.readline().strip().split()))
N_list.sort()
M = int(sys.stdin.readline())
M_list = list(map(int,sys.stdin.readline().strip().split()))
ans = list()

for i in range(M):
    if M_list[i] < N_list[0] or M_list[i] > N_list[N-1]:
        ans.append(0)
        continue
    mid = N//2
    right = N-1
    left = 0
    while True:
        if M_list[i] > N_list[mid]:
            left = mid+1
            if N_list[left] == M_list[i]:
                ans.append(1)
                break
        else :
            right = mid
            if N_list[right] == M_list[i]:
                ans.append(1)
                break
        
        if right == left:
            ans.append(0)
            break

        mid = (right-left)//2+left

print(*ans)