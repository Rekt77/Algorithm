from itertools import combinations
import sys

while True:
    numbers=list(map(int,sys.stdin.readline().strip().split()))
    K, S = numbers[0], numbers[1:]
    if K == 0:
        break
    combi = combinations(S,6)
    for each in combi:
        print(*each)
    print()