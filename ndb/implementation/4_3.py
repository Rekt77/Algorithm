horizontal_order = {alpha:i+1 for i,alpha in enumerate("abcdedfgh")}
X,Y = [int(a) if a.isdigit() else horizontal_order[a] for a in input()]
vectors = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
available = 0

for vector in vectors:
    rowMask=(X+vector[0] > 0 and X+vector[0] < 9)
    colMask=(X+vector[1] > 0 and X+vector[1] < 9)
    if rowMask and colMask:
        available+=1
print(available)