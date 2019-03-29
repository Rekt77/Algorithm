woman, man, intern = map(lambda x : int(x),input().split())

maxTeam = man if (woman//2) > man else (woman//2) 

restWoman, restMan = woman-maxTeam*2, man-maxTeam

if restWoman + restMan >= intern:
    print(maxTeam)

else:
    if (intern -restWoman-restMan) % 3 == 0 :
        maxTeam -= (intern - restWoman - restMan) // 3
    else:
        maxTeam -= (intern - restWoman - restMan) // 3 + 1
    print(maxTeam)
