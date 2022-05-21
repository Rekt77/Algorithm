N = int(input())
nodes = list(map(int,input().split()))
nodes.sort()
K = int(input())
target = list(map(int,input().split()))
for i in range(K):
    right = N-1
    left = 0
    mid = right//2
    flag = 0
    if target[i]>nodes[right]:
        print(flag)
        continue
    while True:
        if nodes[mid] < target[i]:
            left = mid+1
            if nodes[left] == target[i]:
                flag = 1
                break
        else:
            right = mid
            if nodes[right] == target[i]:
                flag = 1
                break
        if right == left or target[i]<nodes[left] or target[i]>nodes[right]:
            break
        mid = (right-left)//2+left
    print(flag)