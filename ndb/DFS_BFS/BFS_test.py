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

def BFS(adj,cur,queue):
    # visited : [1]
    visitedList = [cur]
    # queue : [1]
    queue.append(cur)
    while queue:
        # queue : [], current : 1
        # queue : [8,3], current : 2
        # queue : [7,8], current : 3
        current = queue.pop()
        
        # iter : [2,3,8]
        # iter : [1,7]
        # iter : [1,4,5]
        for nVertex in adj[current]:

            # visited : [1] -> 2, 3, 8 모두 실행
            # visited : [1,2,3,8] -> 7만 실행
            # visited : [1,2,3,8,7] -> 4, 5만 실행
            if not nVertex in visitedList:

                # queue : [8,3,2]
                # queue : [7,8,3]
                # queue : [5,4,7,8,3]
                queue.insert(0,nVertex)
                
                # visited : [1,2,3,8]
                # visited : [1,2,3,8,7]
                # visited : [1,2,3,8,7,4,5]
                visitedList.append(nVertex)
    return visitedList
            

print(*BFS(adj,1,[]))