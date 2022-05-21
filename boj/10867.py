import sys

N = int(sys.stdin.readline())
numbers=sorted(list(set(map(int,sys.stdin.readline().split()))))
for each in numbers:
    print(each,end=" ")