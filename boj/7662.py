import sys
import heapq

N = int(sys.stdin.readline())
for _ in range(N):
    K = int(sys.stdin.readline())
    visited = [0]*K

    max_heap = []
    min_heap = []

    for i in range(K):
        cmd, cmd_v = sys.stdin.readline().strip().split()
        if cmd == "I":
            heapq.heappush(max_heap,(-int(cmd_v),i))
            heapq.heappush(min_heap,(int(cmd_v),i))
            visited[i] = 1
        else :
            if cmd_v == "1":
                while max_heap and visited[max_heap[0][1]] == 0 :
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[heapq.heappop(max_heap)[1]] = 0
            elif cmd_v == "-1":
                while min_heap and visited[min_heap[0][1]] == 0 :
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[heapq.heappop(min_heap)[1]] = 0
                    
    if 1 not in visited:
        print("EMPTY")
    else:
        while max_heap and visited[max_heap[0][1]] == 0 :
            heapq.heappop(max_heap)
        while min_heap and visited[min_heap[0][1]] == 0 :
            heapq.heappop(min_heap)
        print(-max_heap[0][0],min_heap[0][0])