N, K = map(int,input().split())

counter=0

while not N==1:
    if N%K==0:
        N = N//K
    else:
        N-=1
    counter+=1

print(counter)