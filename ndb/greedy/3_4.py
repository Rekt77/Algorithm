N = 27
K = 3
count = 0
while N!=1:
    if N%K == 0:
        N = N//K
    else :
        N -= 1
    count +=1
    print(N)

print(count)