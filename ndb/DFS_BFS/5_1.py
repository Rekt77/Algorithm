def dfs(graph, v, visited,target):
    visited[v] = True
    print(v)
    for i in graph[v]:
        if i == target:
            break
        if not visited[i]:
            dfs(graph, i, visited)

words = ["hot", "dot", "dog", "lot", "log", "cog"]
visited = { word:False for word in words}
graph = {'hot': ['dot', 'lot'], 'dot': ['hot', 'dog', 'lot'], 'dog': ['dot', 'log', 'cog'], 'lot': ['hot', 'dot', 'log'], 'log': ['dog', 'lot', 'cog'], 'cog': ['dog', 'log']}
dfs(graph,words[0],visited)