import sys

N,K = map(int,sys.stdin.readline().split())

hashMap={}
for _ in range(N):
    k,v = sys.stdin.readline().strip().split()
    hashMap[k] = v

for _ in range(K):
    print(hashMap[sys.stdin.readline().strip()])