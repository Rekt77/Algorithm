#price = [0,1,5,8,9,10,17,17,20,24]
price = [0,1,5,8,9]
N = 4
dp = [0]*(N+1)
max_value = 0

#현재 파이프의 길이 == i
#1~9
for i in range(1,N+1):
    #자를 파이프의 길이 == j
    #i값 까지 짜를 수 있음.
    #현재 파이프의 길이가 3이면 3까지
    for j in range(1,i+1):
        dp[i] = max(dp[i],dp[i-j]+price[j])
print(dp[-1])
