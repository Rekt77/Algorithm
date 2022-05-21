import sys

N, M = map(int,sys.stdin.readline().strip().split())
woods = list(map(int,sys.stdin.readline().strip().split()))
start,end = 1,max(woods)

while start<=end:
    logs = 0
    cutter_h = (start+end)//2
    for each in woods:
        if each > cutter_h:
            logs += each-cutter_h

    if logs>=M:
        start = cutter_h + 1
    else:
        end = cutter_h-1

print(end)