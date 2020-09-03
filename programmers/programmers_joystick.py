def solution(name):
    answer = 0
    index=0
    name=list(name)
    while(True):
        right=1
        left=1
        # A는 값을 구할 필요가 없으므로
        if name[index] != 'A':
            # 아래,위 중 효율 적인 방향을 찾음
            updown = min(ord(name[index])-ord('A'),(ord('Z')-ord(name[index])+1))
            answer += updown
        
        #현재 값을 A로 변경
        name[index] = 'A'

        #마지막일 때
        if name == ["A"]*len(name): break


        #오른쪽 문자가 A일 때 right+1
        for i in range(1,len(name)):
            if name[index+i]=="A": right+=1
            else: break

        #왼쪽 문자가 A일 때 left+1
        for i in range(1,len(name)):
            if name[index-i]=="A": left+=1
            else: break
        

        if right>left:
            answer+=left
            index-=left
        else:
            answer+=right
            index+=right
    return answer
print(solution("BBAABBAAB"))