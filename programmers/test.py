import math
def feeCalc(time,fees):
    fee = 0
    total = 0
    if len(time)%2!=0:
        time.append("23:59")
    for i in range(0,len(time),2):
        IN = time[i]
        OUT = time[i+1]
        IN_H, IN_M = map(int,IN.split(":"))
        OUT_H, OUT_M = map(int,OUT.split(":"))
        if OUT_M < IN_M:
            elapsedhour = abs((IN_H+1)-OUT_H)
            elapsedmin = 60-(IN_M-OUT_M)%60
        elif OUT_M == IN_M:
            elapsedhour = abs(IN_H-OUT_H)
            elapsedmin = 0
        else :
            elapsedhour = abs(IN_H-OUT_H)
            elapsedmin = 60-(IN_M-OUT_M)%60
        total += (elapsedhour*60)+elapsedmin
    if total-fees[0] > 0:
        fee += (math.ceil((total-fees[0])/fees[2]))*fees[3]
    fee += fees[1]
    return fee

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
records_dict = dict()
answer = []
for stamp in records:
    time,car,_ = stamp.split()
    if records_dict.get(car):
        records_dict[car].append(time)
    else :
        records_dict[car] = [time]

print(records_dict)

for num,time in records_dict.items():
    answer.append([num,feeCalc(time,fees)])
print(list(list(zip(*sorted(answer)))[1]))
