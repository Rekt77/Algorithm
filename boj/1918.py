import sys

answer = []
operator = []
order = {"*":2,"/":2,"+":1,"-":1,"(":0,")":0}
line = sys.stdin.readline().strip()
idx = 0
while idx<len(line):
    tmp = ""
    while idx<len(line) and line[idx] not in order:
        tmp += line[idx]
        idx += 1
    if tmp != "":
        answer.append(tmp)
        continue
    if line[idx] in order:
        if line[idx] == "(":
            operator.append(line[idx])

        elif line[idx] == ")":
            while operator and operator[-1] != "(":
                answer.append(operator.pop())
            operator.pop()

        else :
            while operator and order[operator[-1]]>=order[line[idx]] :
                answer.append(operator.pop())
            operator.append(line[idx])

    idx += 1

while operator:
    answer.append(operator.pop())
print("".join(answer))