inout= [list(map(int,input().split())) for _ in range(4)]

cur = 0
heads = []
for i in range(4):
    cur += inout[i][1]-inout[i][0]
    heads.append(cur)
    
print(max(heads))