N,M,K = map(int,input().split())
numbers = list(map(int, input().split()))
numbers.sort()

seqlength = (M//(K+1))*K
seqlength += M%(K+1)
number = 0
number += seqlength*numbers[-1]
number += (M-seqlength)*numbers[-2]

print(number)