# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 05:50:11 2019

@author: Rekt77
"""

N = int(input().strip())
scores = [int(input().strip()) for _ in range(N)]
dp = list()
dp.append(scores[0])
dp.append(dp[0]+scores[1])
dp.append(max(scores[2]+scores[0],scores[2] + scores[1]))

# 현재 밟고 있는 계단을 오르기 위해서는 전과 전전전의 계단을 밟았거나 전전의 계단을 밟음
for i in range(3,N):
    dp.append(max(scores[i] + dp[i-2], scores[i]+scores[i-1] + dp[i-3]))
    
print(dp[-1])