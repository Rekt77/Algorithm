import sys

N,r,c = map(int,sys.stdin.readline().strip().split())

tile = []
counter = 0
flag = True
for i in range((2**N)):
    tmp = []
    for j in range((2**N)):
        tmp.append((i,j))
    tile.append(tmp)

def divide_conquer(tile,r,c):
    global counter
    global flag
    if len(tile) == 1:
        if tile[0][0][0] == r and tile[0][0][1] == c :
            print(counter)
            flag=False
        counter += 1
        return 1

    s1 = [each[:len(tile)//2] for each in tile[:len(tile)//2]]
    s2 = [each[len(tile)//2:] for each in tile[:len(tile)//2]]
    s3 = [each[:len(tile)//2] for each in tile[len(tile)//2:]]
    s4 = [each[len(tile)//2:] for each in tile[len(tile)//2:]]

    for each_square in [s1,s2,s3,s4]:
        if flag == True:
            divide_conquer(each_square,r,c)

divide_conquer(tile,r,c)