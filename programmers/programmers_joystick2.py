def isAstream(idx,word,mode):
    if idx>=len(word):
        return 0
    cur = word[idx]
    count = 0
    while cur == "A":
        count += 1
        idx += mode
        if idx>=len(word):
            break
        cur = word[idx]
    return count

def changeCounter(src,dst):
    return min((ord(src)-ord(dst))%26,(ord(dst)-ord(src))%26)

def solution(name):    
    word = ["A"]*len(name)
    target = list(name)
    counter = []
    for i in range(len(word)):
        counter.append(changeCounter(word[i],target[i]))

    mode = 1
    count = 0
    cur_idx = 0

    while True:
        count += counter[cur_idx]
        counter[cur_idx] = 0
        if sum(counter) == 0:
            break
        if isAstream(cur_idx+mode,target,mode)>=1:
            A_count = isAstream(cur_idx+mode,target,mode)
            if A_count+1 <= len(word)-(A_count+1):
                mode = 1
                count += A_count+1
            else :
                mode = -1
                count += len(word)-(A_count+1)
            cur_idx += A_count+1
        else :
            cur_idx += mode
            count += 1
    return count

print(solution("BBAABBAAB"))