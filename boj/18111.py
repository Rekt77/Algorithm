import sys
N,M,B= map(int,sys.stdin.readline().strip().split())
blocks = []
time = 0
ans = 640000000
for i in range(N):
    blocks+=list(map(int,sys.stdin.readline().strip().split()))

#기준 높이 설정하고 높은애는 깎고, 낮은애는 더하고
#핵심은 깎은 애들을 통해 낮은애를 기준높이만큼 만들 수 있는가
for i in range(257):
    add = 0
    rm = 0
    for j in range(N*M):
        if i>blocks[j]:
            add += i-blocks[j]
        else:
            rm += blocks[j]-i
    inventory = rm + B
    if inventory < add:
        continue
    
    time = 2 * rm + add

    if time<=ans:
        ans = time
        curH = i

print(ans,curH)
                
