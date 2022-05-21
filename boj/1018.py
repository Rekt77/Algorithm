import sys
h, w = map(int,sys.stdin.readline().strip().split())
board = [list(sys.stdin.readline().strip()) for _ in range(h)]

kernel = []
answer = []
component = ["B","W"]
for _ in range(2):
    tmp = []
    for _ in range(8):
        tmp.append(component*4)
        component.append(component.pop(0))
    component = ["W","B"]
    kernel.append(tmp)

for k in range(2):
    ypos,xpos = 0,0
    while ypos+8<=h:
        counter = 0
        for y in range(ypos,ypos+8):
            for x in range(xpos,xpos+8):
                if board[y][x] != kernel[k][y-ypos][x-xpos]:
                    counter += 1
        if xpos+8>=w:
            xpos = 0
            ypos += 1
        else:
            xpos += 1
        answer.append(counter)
print(min(answer))