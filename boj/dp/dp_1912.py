# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:26:54 2019

@author: tgb
"""

N = int(input())
numbers = list(map(int,input().strip().split()))

dp =[0 for _ in range(N)]
dp[0] = numbers[0]
for i in range(1,N):
    dp[i] = max(dp[i-1] + numbers[i],numbers[i])

print(max(dp))