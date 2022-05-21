H, M= map(int,input().split())

flag = True if M-45<0 else False
if flag:
    H = (24+H-1)%24
M = (60+M-45)%60
print(H,M)