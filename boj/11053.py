import sys

N = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().strip().split()))
dp = [1]*N

for i in range(N):
    for j in range(i):
        if numbers[j]<numbers[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))