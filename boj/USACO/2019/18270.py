N = int(input())
lines = [input() for _ in range(N)]
ans = [lines[0].split()[0],lines[0].split()[-1]]
for each in lines[1:]:
    if each.split()[0] in ans:
        
    elif each.split()[-1] in ans:


        



print(lines)