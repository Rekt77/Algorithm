import sys
Ncase = int(sys.stdin.readline().strip())
sys.setrecursionlimit(10**5)

def dfs(vertex,colored):
    color[vertex-1] = colored
    for k in adj[vertex-1]:
        if color[k-1] == 0: 
            dfs(k,colored*-1)


def check():
    for k in range(len(adj)):
        for v in adj[k]:
            if color[k] == color[v-1]:
                return False
    return True

for _ in range(Ncase):
    Nvertex, Nline = map(int,sys.stdin.readline().strip().split())
    adj = [[] for _ in range(Nvertex)]
    color = [0]*Nvertex

    for _ in range(Nline):
        vertex, adj_vertex = map(int,sys.stdin.readline().strip().split())
        adj[vertex-1].append(adj_vertex)
        adj[adj_vertex-1].append(vertex)

    for i in range(1,Nvertex+1):
        if color[i-1] == 0:
            dfs(i,1)
            
    print("YES" if check() else "NO")