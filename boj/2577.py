A,B,C = [int(input()) for _ in range(3)]
freq = dict()
for each in str(A*B*C):
    each = int(each)
    if freq.get(each):
       freq[each] +=1
    else:
        freq[each]=1

for i in range(10):
    if freq.get(i):
        print(freq[i])
    else:
        print(0)
