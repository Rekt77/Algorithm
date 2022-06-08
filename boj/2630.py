#2630.py
import sys

N = int(sys.stdin.readline().strip())
board = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
#N = 8
#board = [[1,1,0,0,0,0,1,1],
#[1,1,0,0,0,0,1,1],
#[0,0,0,0,1,1,0,0],
#[0,0,0,0,1,1,0,0],
#[1,0,0,0,1,1,1,1],
#[0,1,0,0,1,1,1,1],
#[0,0,1,1,1,1,1,1],
#[0,0,1,1,1,1,1,1]]

def conquered(board):
    res = 0
    N = len(board)
    for i in range(N):
        res += sum(board[i])
    res = res if res==0 or res==N*N else -1
    return res
  
  
def divide(board,blue=0,white=0):
    N = len(board)
    if N == 1:
      if board[0][0] == 0:
        white+=1
      else :
        blue+=1  
      return white,blue

    res = conquered(board)
    if res != -1:
      if res == 0:
        white+=1
      else:
        blue+=1
      return white,blue

    s1 = [ each[:N//2] for each in board[:N//2]]
    s2 = [ each[N//2:] for each in board[:N//2]]
    s3 = [ each[:N//2] for each in board[N//2:]]
    s4 = [ each[N//2:] for each in board[N//2:]]
    
    for each in [s1,s2,s3,s4]:
        white,blue = divide(each,blue,white)
    return white,blue

white, blue = divide(board)
print(white)
print(blue)
