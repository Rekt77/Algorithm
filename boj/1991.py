N = int(input())
nodes = dict()
for _ in range(N):
    route = input().split()
    nodes[route[0]] = [route[1],route[2]]

def pre_search(cur):
    if cur == ".":
        return 0
    #cur = A
    print(cur,end="")
    pre_search(nodes[cur][0])
    pre_search(nodes[cur][1])

def post_search(cur):
    if cur == ".":
        return 0
    #cur = A
    post_search(nodes[cur][0])
    print(cur,end="")
    post_search(nodes[cur][1])

def mid_search(cur):
    if cur == ".":
        return 0
    #cur = A
    mid_search(nodes[cur][0])
    mid_search(nodes[cur][1])
    print(cur,end="")


pre_search("A")
print("")
post_search("A")
print("")
mid_search("A")

    