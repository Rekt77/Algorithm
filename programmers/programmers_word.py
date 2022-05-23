answer = 0
def isChangable(src,trg):
    diff = 0
    if src==trg:
        return 0
    for i in range(len(src)):
        if src[i] != trg[i]:
            diff+=1
    if diff < 2:
        return 1
    else :
        return 0
    
def endDiagonal(trg,words):
    if trg not in words:
        return 1
    return 0

def dfs(cur,words,target,visited=[],count=0):
    visited.append(cur)
    if cur == target:
        global answer
        answer = count
    for each in words:
        if each not in visited and isChangable(cur,each):
            dfs(each,words,target,visited,count+1)

def solution(begin, target, words):
    if endDiagonal(target, words):
        return 0
    dfs(begin,words,target)
    return answer

words = ["hot", "dot", "dog", "lot", "log", "cog"]
target = "cog"
begin = "hit"
print(solution(begin,target,words))
