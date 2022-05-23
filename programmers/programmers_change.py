def isChangable(word,tar):
    tmp = []
    for i in range(len(word)) :
        if word[i] != tar[i]:
            tmp.append(True)
    if sum(tmp) == 1:
        return True
    else :
        return False
words = ["hot", "dot", "dog", "lot", "log", "cog"]
adj = {word:[] for word in words}
for i in range(len(words)):
    for j in range(len(words)):
        if words[i] != words[j]:
            if isChangable(words[i],words[j]):
                adj[words[i]].append(words[j])
print(adj)

begin = "hit"
target = "cog"
visited = []
stack = [begin]
while stack:
    current = stack.pop()
    for neighbor in adj[current]:
        if neighbor not in visited:
            stack.append(neighbor)
            if stack[-1] == target:
                print(stack)
    print("stack",stack)
    visited.append(current)
    print("vis",visited)
    
    