import string

def recursion(msg,idx,dic):
    if msg[:idx]!=msg[:idx+1] and msg[:idx] in dic:
        number,msg = recursion(msg,idx+1,dic)
    else :
        if msg[:idx] in dic:
            number = dic.index(msg[:idx])+1
            msg = ""
        else:            
            dic.append(msg[:idx])
            number = dic.index(msg[:idx-1])+1
            msg = msg[idx-1:]
    return number, msg

def solution(msg):
    answer = []
    zdic = list(string.ascii_uppercase)
    while msg:
        number, msg=recursion(msg,1,zdic)
        answer.append(number)
    return answer