# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 05:19:04 2019

@author: Rejt77
"""

#import sys

N = int(input())

level = [list(map(int,input().strip().split())) for _ in range(N)]
dp = [[level[0][0]]]+[list() for _ in range(N-1)]


for i in range(1,N):
    for j in range(0,i+1):
        if j == 0:
            dp[i].append(level[i][j]+dp[i-1][j])
        
        elif i == j:
            dp[i].append(level[i][j]+dp[i-1][j-1])
        
        else:
            dp[i].append(level[i][j] + max(dp[i-1][j-1], dp[i-1][j]))
            
print(max(dp[-1]))