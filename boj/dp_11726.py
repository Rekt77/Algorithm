# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 00:40:56 2019

@author: Rekt77
"""

N = int(input().strip()) 
dp = [1,2]

for i in range(2,N):
    dp.append(dp[i-1] + dp[i-2])

if(N ==1):
    print(dp[0])
elif(N==2):
    print(dp[1])
else:
    print(dp[-1]%10007)
    