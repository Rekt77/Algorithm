kg = int(input())
if kg in [1,2,4,7]:
    print(-1)
elif kg%5==1 or kg%5==3:
    print(kg//5+1)
elif kg%5==2 or kg%5==4:
    print(kg//5+2)
else:
    print(kg//5)