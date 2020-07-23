V,E,start = map(int,input().split())
edgeList = []
for _ in range(E):
    c,n = map(int,input().split())
    edgeList.append((c,n))

adj = {i+1:[] for i in range(V)}

for edge in edgeList:
    adj[edge[0]].append(edge[1])
    adj[edge[1]].append(edge[0])

for k in adj.keys():
    adj[k].sort()

def BFS(adj,current):
    visited = [current]
    queue = [current]
    while queue:
        current = queue.pop()
        for nVertex in adj[current]:
            if not nVertex in visited:
                queue.insert(0,nVertex)
                visited.append(nVertex)
    return visited

dfs_visited = []

def DFS(adj,start,visited):
    visited.append(start)
    for each in adj[start]:
        if not each in visited:
            DFS(adj,each,visited)

DFS(adj,start,dfs_visited)
print(*dfs_visited)
print(*BFS(adj,start))