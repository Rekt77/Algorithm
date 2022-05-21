N, L = map(int,input().split())
adj = { i+1:[]for i in range(N)}
for _ in range(L):
    v1,v2 =map(int,input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

def DFS(adj,c,visited):
    if not c in visited:
        visited.add(c)
        for v in adj[c]:
            DFS(adj,v,visited)
        

visited = set()
counter = 0

for i in range(1,N+1):
    if not i in visited:
        counter += 1
        DFS(adj,i,visited)

print(counter)
