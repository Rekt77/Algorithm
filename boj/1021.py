import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
target = list(map(int,sys.stdin.readline().split()))
numbers = deque([ i for i in range(1,n+1)])
cnt = 0

for i in range(m):
    lshift = (numbers.index(target[i]))%n
    rshift = abs(numbers.index(target[i])-n)
    while target:
        if target[i] == numbers[0]:
            numbers.popleft()
            n -= 1
            break
        #do rshift
        if lshift > rshift:
            numbers.appendleft(numbers.pop())
            cnt += 1
        #do lshift    
        else:
            numbers.append(numbers.popleft())
            cnt += 1
print(cnt)