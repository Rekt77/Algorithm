import sys

K, N = map(int,sys.stdin.readline().strip().split())
utps = [int(sys.stdin.readline()) for _ in range(K)]
high = max(utps)
low = 1

#이분 탐색
while low<=high:
    mid = (high+low)//2

    epoch_N=sum([each//mid for each in utps])
    if epoch_N < N :
        high = mid-1

    elif epoch_N >= N:
        low = mid+1


print(high)