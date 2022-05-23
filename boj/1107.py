import sys
target = int(sys.stdin.readline().strip())
nBroken = int(sys.stdin.readline())
Broken = list(map(int,sys.stdin.readline().strip().split())) if nBroken != 0 else []
Broken_TF = [True]*10
min_diff = 99999999

for number in Broken:
    Broken_TF[number] = False

def button_max(target):
    for i in str(target):
        if Broken_TF[int(i)] == False:
            return False
    return True

for i in range(1000001):
    if button_max(i):
        min_diff = min(min_diff,abs(target-i)+len(str(i)))

min_diff=min(min_diff,abs(target-100))
print(min_diff)