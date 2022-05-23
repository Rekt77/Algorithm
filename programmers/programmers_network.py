#adj list에서 연결된 그래프 찾는법
#visited 처리를 해야함

def dfs(cur,adj,counter=0):
    #0,1,0
    visited.add(cur)
    print(visited)
    for i in range(len(adj[cur])):
        if adj[cur][i] == 1 and i not in visited:
            counter = dfs(i,adj,counter)
            counter += 1
    return counter
"""
def solution(n, computers):
    answer = 0

    dfs(0,adj)
    return answer
"""
#computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
computers =[[1,1,0,0,0,0,0,0,0],
[1,1,0,0,0,0,0,0,0],
[0,0,1,1,0,0,0,0,0],
[0,0,1,1,0,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,1,1,0,0,],
[0,0,0,0,0,1,1,1,0],
[0,0,0,0,0,0,1,1,1],
[0,0,0,0,0,0,0,1,1]]
