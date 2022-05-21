N = int(input())
if N//10 == 0:
    if N%2==0:
        print(N//2)
    else:
        print(0)

thresh = 9*(N//10)
new = int(N)-thresh
for i in range(new,N):
    sum=0
    for each in str(i):
        sum+=int(each)
    sum+=i
    if sum==N:
        print(i)
        break
    if i==N-1:
        print(0)
        break