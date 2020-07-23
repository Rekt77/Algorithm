N = int(input())
houseMap = []
cp = {}
for _ in range(N):
    tmp = []
    for i in input():
        tmp.append(int(i))
    houseMap.append(tmp)

def hasAdj(houseMap,i,j):
    adj = []
    d = [(0,-1),(0,1),(-1,0),(1,0)]
    for y,x in d:
        try:
            if i+y>=0 and j+x>=0:
                if houseMap[i+y][j+x] == 1 :
                    adj.append((i+y,j+x))
        except IndexError:
            pass
    return adj

for i in range(N):
    for j in range(N):
        if houseMap[i][j] == 1:
            cp[(i,j)]=hasAdj(houseMap,i,j)

def DFS(adj,c,hist):
    for v in adj[c]:
        if not v in hist:
            hist.add(v)
            DFS(adj,v,hist)
    return hist
#Search
master = set()
cluster = []
for v in cp.keys():
    if not v in master:
        res = DFS(cp,v,set())
        master.update(res)
        cluster.append(len(res))


print(len(cluster))
cluster.sort()
for i in cluster:
    if i == 0:
        print(1)
    else:
        print(i)

#for i in range(N):
#    for j in range(N):
#        try:
#            print(cp[i][j].my,cp[i][j].adj)
#        except:
#            pass