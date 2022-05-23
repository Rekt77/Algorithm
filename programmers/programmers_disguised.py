clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"],["blacksunglasses", "eyewear"]]

hash = dict()
for item,cat in clothes:
    if hash.get(cat):
        hash[cat].append(item)
    else :
        hash[cat] = [item]
print(hash)
answer = 1
for key in hash.keys():
    answer *= len(hash[key])+1

print(answer-1)