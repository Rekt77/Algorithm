N = int(input().split()[0])
commands = input().split()

vectors = {
    "U":(-1,0),
    "D":(1,0),
    "R":(0,1),
    "L":(0,-1)
    }

travler = [1,1]
board = (N,N)

for command in commands:
    X = travler[0]+vectors[command][0]
    Y = travler[1]+vectors[command][1]
    if( (X >= 1 and X<=N) and (Y >= 1 and Y<=N)):
        travler[0] += vectors[command][0]
        travler[1] += vectors[command][1]

print(travler)