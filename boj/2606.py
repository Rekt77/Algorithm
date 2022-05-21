import sys
sys.setrecursionlimit(20000)

N = int(input())
L = int(input())
adj = {i+1:[] for i in range(N)}
for i in range(L):
    v1, v2 = map(int,input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

def DFS(adj,c,visited):
    if not c in visited:
        visited.add(c)
        for v in adj[c]:
            DFS(adj,v,visited)
    return visited


print(len(DFS(adj,1,set()))-1)