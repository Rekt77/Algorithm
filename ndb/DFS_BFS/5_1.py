H,W = map(int,input().split())

ice = [ input() for _ in range(H)]
adj = dict()

def adjCheck(x,y):
    vectors = [(1,0),(0,1),(-1,0),(0,-1)]
    neighbor = []
    for v in vectors:
        try:
            if (x+v[0]<0 or y+v[1]<0):
                continue
            if ice[x+v[0]][y+v[1]] == "0":
                neighbor.append((x+v[0],y+v[1]))
        except IndexError:
            pass
    adj[(x,y)] = neighbor

def DFS(adj,c,hist):
    if not c in hist:
        hist.add(c)
        for v in adj[c]:
            DFS(adj,v,hist)
    return hist

for i in range(H):
    for j in range(W):
        if ice[i][j]=="0":
            adjCheck(i,j)

hist = set()
counter=0
for i in range(H):
    for j in range(W):
        if not (i,j) in hist and ice[i][j]=="0":
            hist.update(DFS(adj,(i,j),set()))
            counter+=1

print(counter)