
visited = set()
adj = {
    1:[2,3,8],
    2:[1,7],
    3:[1,4,5],
    4:[3,5],
    5:[3,4],
    6:[7],
    7:[2,6,8],
    8:[1,7]
}

def DFS(adj,c,visited):
    # DFS(1)
    # {1}
    visited.add(c)
    print(c,end=" ")

    # 2 3 8
    for i in adj[c]:
        if i not in visited:
            # recursive of 2
            # DFS(2) -> # DFS(7)  -> # DFS(6)
            # {1,2}  -> # {1,2,7} -> # {1,2,6,7}
            #                     -> # DFS(8)
            #                     -> # {1,2,6,7,8}
            #
            # recursive of 3
            # DFS(3)        -> # DFS(4)          -> # DFS(5)
            # {1,2,3,6,7,8} -> # {1,2,3,4,6,7,8} -> # {1,2,3,4,5,6,7,8}
            #
            # recrusive of 8
            # 이미 방문했기때문에 아무일도 일어나지 않음
            DFS(adj, i, visited)

DFS(adj,1,visited)