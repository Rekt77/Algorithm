import sys

N = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().strip().split()))
ans = 0
for each in numbers:
    if each==1:
        continue
    if each==2 or each==5 or each==3:
            ans +=1
            continue
    if each%2!=0:

        for i in range(3,each//2+1,2):
            if each%i==0:
                break
            if i==each//2 or i==each//2-1:
                ans += 1

print(ans)