import sys, string

knight = sys.stdin.readline()
vectors = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
count = 0
for v in vectors:
    col = ord(knight[0])
    row = int(knight[1])
    if 0<row+v[0]<9 and ord("a")<=col+v[1]<=ord("h"):
        print(chr(col+v[1])+str(row+v[0]))
        count +=1
print(count)