"""def solution(prices):
    answer = [0]*len(prices)
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[i]<=prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer"""

def solution(prices):
    answer = [0]*len(prices)
    stack = []
    for i,price in enumerate(prices):
        while stack and price<prices[stack[-1]]:
            idx = stack.pop()
            answer[idx] = i - idx
        stack.append(i)
        
    while stack:
        idx = stack.pop()
        answer[idx] = len(prices) - idx - 1
        
    return answer

solution([1, 2, 3, 2, 3])