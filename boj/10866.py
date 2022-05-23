#push_front X: 정수 X를 덱의 앞에 넣는다.
#push_back X: 정수 X를 덱의 뒤에 넣는다.
#pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#size: 덱에 들어있는 정수의 개수를 출력한다.
#empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
#front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
from collections import deque

n = int(sys.stdin.readline())
dequeue = deque()
cnt = 0
for _ in range(n):
    cmd = sys.stdin.readline()
    if cmd.startswith("push_front"):
        dequeue.appendleft(int(cmd.split()[1]))
        cnt +=1
        continue
    elif cmd.startswith("push_back"):
        dequeue.append(int(cmd.split()[1]))
        cnt +=1
        continue
    elif cmd.startswith("pop_front"):
        if dequeue:
            answer = dequeue.popleft()
            cnt -=1
        else :
            answer = -1
    elif cmd.startswith("pop_back"):
        if dequeue:
            answer = dequeue.pop()
            cnt -=1
        else :
            answer = -1
    elif cmd.startswith("size"):
        answer = cnt
    elif cmd.startswith("empty"):
        answer = 0 if dequeue else 1
    elif cmd.startswith("front"):
        answer = dequeue[0] if dequeue else -1
    elif cmd.startswith("back"):
        answer = dequeue[-1] if dequeue else -1
    print(answer)