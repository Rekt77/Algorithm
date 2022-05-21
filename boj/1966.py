import sys

case = int(sys.stdin.readline())

for i in range(case):
    N, target = map(int,sys.stdin.readline().strip().split())
    printer = list(zip(map(int,sys.stdin.readline().strip().split()),[i for i in range(N)]))
    counter = 0
    while True:
        if printer[0] == max(printer,key=lambda x : x[0]):
            ans = printer.pop(0)
            counter += 1
            if ans[1]==target:
                print(counter)
                break
        else:
            printer.append(printer.pop(0))
