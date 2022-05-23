from itertools import permutations

def solution(numbers):
    
    result = map(lambda x : int("".join(x)),list(permutations(map(lambda x: str(x), numbers),len(numbers))))
    answer = str(max(result))
    
    return answer

print(solution([6,10,2,10,2,9,2,3,4,5,7,7,5,4,3,2,12,4,43,213,45,243,45,234,5,234,2,34,523,45,234,5,23,12,3]))