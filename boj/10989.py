import sys

myList = [0]*100001
N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    myList[num] = myList[num]+1

for i in range(10001):
    if myList[i] != 0:
        for _ in range(myList[i]):
            print(i)