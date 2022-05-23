from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for num in course:
        order_combinations = []
        for order in orders:
            for temp in combinations(order, num):
                order_combinations.append(''.join(sorted(temp)))
            
        order_counter = Counter(order_combinations).most_common()
        
        maximum = 0
        for order in order_counter:
            if maximum <= order[1]:
                maximum = order[1]
    
        for order in order_counter:
            if maximum <= order[1] and 2 <= order[1]:
                answer.append(order[0])

    return sorted(answer)

def solution2(orders, course):
    answer = []
    for each in course:
        all_combi = []
        for order in orders:
            combi = combinations(order,each)
            all_combi.extend(list(map(lambda x: "".join(x),sorted(combi))))
        count = Counter(all_combi).most_common()
        max = 0
        for k,v in count:
            if max<=v:
                max = v
        for k,v in count:
            if max <= v and 2 <= v:
                answer.append(k)
    return sorted(answer)


print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))
print(solution2(["XYZ", "XWY", "WXA"],[2,3,4]))