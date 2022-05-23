import sys
N = int(sys.stdin.readline())
commands = sys.stdin.readline().strip().split()
c2vec = {"R":(0,1),"L":(0,-1),"U":(-1,0),"D":(1,0)}
init = (1,1)
for cmd in commands :
    if (init[0]+c2vec[cmd][0])>0 and (init[1]+c2vec[cmd][1])>0:
        init = (init[0]+c2vec[cmd][0],init[1]+c2vec[cmd][1])

print(init[0],init[1])