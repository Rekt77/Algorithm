dp = [1,1]

N = int(input())

for i in range(2,N):
    dp.append(dp[i-1]+dp[i-2])
print(dp[-1])