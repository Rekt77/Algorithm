counter = 0

N = input()

for h in range(int(N)+1):
    for m in range(60):
        for s in range(60):
            if "3" in "%s%s%s"%(h,m,s):
                counter += 1

print(counter)