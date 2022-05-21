import sys

N = int(sys.stdin.readline())
xylist = list()
for _ in range(N):
    line = sys.stdin.readline().strip().split()
    xylist.append((int(line[0]), int(line[1])))

xylist.sort(key=lambda x: (x[1], x[0]))
for each in xylist:
    print(each[0], each[1])