n, weight = map(int, input().split())
n, weight = 4, 7
arr = [(0, 0)]

for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

dp = [[0]*(weight+1) for _ in range(n+1)]

for i in range(1,n+1):
    w, v = arr[i][0], arr[i][1]
    for j in range(1,weight+1):
        # 못집어 넣는 경우
        if j < w:
            # 바로 전단계의 최댓값에 따른다
            dp[i][j] = dp[i-1][j]
        else :
            dp[i][j] = max(dp[i-1][j-w]+v,dp[i-1][j])

print(dp[-1][-1])