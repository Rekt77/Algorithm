changes = [500,100,50,10]

N = int(input())
coins = 0

# 핵심은 큰 돈부터 주는 것
for change in changes:
    if not N == 0:
        count = N//change
        N -= (change*count)
        coins += count
print(coins)
    