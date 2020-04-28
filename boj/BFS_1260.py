class Stack:
    stack = []
    def push(self,object):
        self.stack.append(object)
    def pop(self):
        return self.stack.pop()

class Queue:
    queue = []
    def enqueue(self,object):
        self.queue.append(object)
    def dequeue(self):
        return self.queue.pop(0)

V,E,start = map(int,input().split())
edgeList = []
for _ in range(E):
    c,n = map(int,input().split())
    edgeList.append((c,n))

adjacencyList = [[] for _ in range(V)]

for edge in edgeList:
    adjacencyList[edge[0]-1].append(edge[1])

print(V,E,at)
print(edgeList)
print(adjacencyList)
visitedVertex =[]
stack = Stack()
queue = Queue()

def DFS(start)
for i in range(V):
    if start in visitedVertex:
    for neighbor in adjacencyList[cur-1]:
        if not neighbor in visitedVertex:
            DFS(neighbor)
    