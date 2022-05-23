def solution(array, commands):
    answer = []
    for i,j,k in commands:
        tmp = sorted(array[i-1:j])
        answer.append(tmp[k-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2,5,3]]))