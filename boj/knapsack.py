I, W = map(int,input().split())
items = [tuple(map(int,input().split())) for _ in range(I)]

dp = [[0]*(W+1) for _ in range(I)]

for idx,item in enumerate(items):
    #가방안에 담긴 물건을 이터레이팅.
    #가방의 무게제한은 처음부터 W로 주는게 아니라, 0~W까지 올려가면서 확인함.
    for w_limit in range(W+1):
        #현재 가방의 수용무게 - 현재 아이템의 무게가 0 또는 양수일 경우
        #만약 현재 가방의 수용무게가 현재 아이템의 무게보다 작으면, 가방에 넣을 수 없기 때문
        if w_limit - items[idx][0] >= 0:
            # 첫번째 아이템인 경우 무게만 맞으면 무조건 가방에 넣는게 최댓값.
            if idx==0:
                dp[idx][w_limit] = items[idx][1]
            # 첫번째 아이템이 아닌 경우
            else:
                #가방의 수용무게 - 현재아이템의 무게 = 잔여 수용무게
                #EX>무게제한 7이고, 물건 무게 4일 경우, 3이 잔여 수용무게
                #결론 적으로 3을 더 넣을 수 있는것임.
                #가방의 수용무게가 3일 때의 최댓값은 이미 구해놨음
                #만약 이 아이템을 넣는다면, 잔여 수용무게가 3일 때 최댓값 + 현재 아이템의 가치 => 현재 수용무게에서 최댓값
                on = dp[idx-1][w_limit-items[idx][0]] + items[idx][1]

                #만약 이 아이템을 넣지 않는다면, 현재 잔여 수용무게에서의 최댓값은 이전 아이템을 넣었을 때 까지임.
                off = dp[idx-1][w_limit]

                #이거 두개를 비교해서 누가 더 최대인지 보고
                #최대인 수를 삽입
                dp[idx][w_limit] = max(on,off)

        #만약 현재 가방의 수용무게 - 현재 아이템의 무게가 음수일 경우
        else :
            # 첫번째 아이템이 아닐 경우
            # 이전 최대값을 사용
            if idx >=1 :
                dp[idx][w_limit] = dp[idx-1][w_limit]

# 결과값 가장 우측 하단의 값이 최대값
print(dp[I-1][W])