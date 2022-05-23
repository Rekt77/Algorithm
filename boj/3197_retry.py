av = 0
def findL(map,R,C):
    L = []
    for i in range(R):
        for j in range(C):
            if map[i][j] == "L":
                L.append((i,j))
        if len(L) == 2:
            return L

def meeting(map,L1,visited=[]):
    global av
    visited.append(L1)
    y, x = L1
    vector = [(0,-1),(0,1),(-1,0),(1,0)]
    for vy, vx in vector:
        if (x+vx >= 0 and x+vx<len(map[0])) and (y+vy>=0 and y+vy<len(map)) and map[y+vy][x+vx] != "X" and (y+vy,x+vx) not in visited:
            if map[y+vy][x+vx] == "L":
                av  = 1
            meeting(map,(y+vy,x+vx),visited)
    return 0

def icemelt(map):
    meltyx = set()
    vector = [(0,-1),(0,1),(-1,0),(1,0)]
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] != "X":
                for vy, vx in vector : 
                    if (j+vx >= 0 and j+vx<len(map[0])) and (i+vy>=0 and i+vy<len(map)) and map[i+vy][j+vx] == "X":
                        meltyx.add((i+vy,j+vx))
    for y,x in meltyx:
        map[y][x] = "."
    return map

R, C = map(int,input().split())
MAP = [ list(input()) for _ in range(R)]
#MAP = ["...XXXXXX..XX.XXX",
#       "....XXXXXXXXX.XXX",
#       "...XXXXXXXXXXXX..",
#       "..XXXXX.LXXXXXX..",
#       ".XXXXXX..XXXXXX..",
#       "XXXXXXX...XXXX...",
#       "..XXXXX...XXX....",
#       "....XXXXX.XXXL..."]
#MAP = list(map(list,MAP))

L1, L2 = findL(MAP,R,C)
day = 0
while True:
    meeting(MAP,L1,visited=[])
    if av == 1:
        break
    day += 1
    MAP = icemelt(MAP)
print(day)