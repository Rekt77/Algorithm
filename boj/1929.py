import sys
N, K = map(int,sys.stdin.readline().strip().split())
numbers = [i for i in range(2,K+1)]
prime = []
for j in range(0,K-1):
    if numbers[j] != 0 :
        radix=numbers[j] 
        if N <= radix:
            prime.append(str(radix))
    else:
        continue
    for i in range(j+radix,K,radix):
        try:
            numbers[i]=0
        except IndexError:
            pass

print("\n".join(prime))