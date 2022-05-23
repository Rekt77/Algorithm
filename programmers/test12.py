#id_list = ["muzi", "frodo", "apeach", "neo"]
id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
#report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","muzi neo","apeach muzi"]
k = 2
answer = [0]*len(id_list)
reportedby = { id:[] for id in id_list}
for each in report:
    src,trg = each.split()
    if src not in reportedby[trg]:
        reportedby[trg].append(src)

for each in reportedby.values():
    if len(each) >= k:
        for id in each:
            answer[id_list.index(id)] += 1

print(reportedby)
print(answer)
