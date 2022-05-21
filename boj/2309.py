from itertools import combinations

a = [int(input()) for _ in range(9)]
combi = combinations(a,7)
    
for res in list(combi):
    if sum(res)==100:
        for each in sorted(res):
            print(each)
        break