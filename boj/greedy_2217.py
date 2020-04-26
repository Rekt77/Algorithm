#Author Rekt77
import sys

N = int(input())
given = [int(sys.stdin.readline()) for _ in range(N)]
given.sort(reverse=True)
result = []

for i in range(0,len(given)):
    result.append((i+1)*given[i])
print(max(result))