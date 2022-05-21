import sys
N = int(sys.stdin.readline().strip())
counter = 0
i = 666
while counter != N:
    if str(i).find("666") >= 0:
        counter += 1
    i += 1
print(i-1)