import sys

N, M = map(int,sys.stdin.readline().strip().split())

def factorial(number):
    if number == 0:
        return 1
    ans = number*factorial(number-1)
    return ans

#print(factorial(100))

ans = factorial(N)//(factorial(N-M)*factorial(M))
print(ans)