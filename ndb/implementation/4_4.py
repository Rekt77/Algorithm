mapX,mapY = map(int,input().split())
curX,curY,cur_side = map(int,input().split())

foward_order = [(-1,0),(0,1),(1,0),(0,-1)]
visited = 1
end_flag = True
myMap = list()
for _ in range(mapY):
    myMap.append(list(map(int,input().split())))

# Rule
# how to turn
# left side == 0->3->2->1->0->3.....
# cur = 0, 0 + 3 % 4, next = 3
# cur = 3, 3 + 3 % 4, next = 2
# cur = 2, 2 + 3 % 4, next = 1
# cur = 1, 1 + 3 % 4, next = 0
while end_flag:
    for i in range(4):
        cur_side = (cur_side + 3) % 4
        rX, rY= foward_order[cur_side]
        try:
            if(myMap[curX+rX][curY+rY] == 0):
                visited+=1
                myMap[curX][curY] = 2
                curX, curY = curX+rX, curY+rY
               # 4번회전하고 갈방향이 있는경우에는 무조건 여기에 걸리게 되어 있음.
                break
            else:
                if i==3:
                    cur_side = (cur_side + 3) % 4
                    rX, rY= foward_order[cur_side]
                    try:
                        if myMap[curX-rX][curY-rY] == 2:
                            curX, curY = curX-rX, curY-rY
                        else:
                            end_flag = False
                    except IndexError:
                        end_flag = False
                else:
                    continue
        except IndexError:
            continue
        # 방향전환으로 초기방향 유지한 후 뒤쪽이 바다칸이 아닌경우(가봤지만 육지인 경우, 여기서는 2에 해당함)
        # 뒤로 한칸갑니다.

print(visited)