N, M = map(int,input().split())
mymap = [ list(map(int,input())) for _ in range(N)]
queue = []
vectors = [(1,0),(0,1),(-1,0),(0,-1)]

queue.insert(0,(0,0))
while queue:
    n,m = queue.pop()
    for v in vectors:
        nx = n+v[0]
        ny = m+v[1]
        try:
            if mymap[nx][ny]==0:
                continue
            if nx >= 0 and ny>=0 and mymap[nx][ny]==1:
                mymap[nx][ny] = mymap[n][m]+1
                queue.insert(0,(nx,ny))
        except IndexError:
            pass

print(mymap)
print(mymap[N-1][M-1])