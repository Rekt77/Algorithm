import sys

cmd = sys.stdin.readline().strip().split("-")
answer = []
for minus in cmd:
    tmp = 0
    plus = minus.split("+")
    for each in plus:
        tmp += int(each)
    answer.append(tmp)

print(answer[0]-sum(answer[1:]))