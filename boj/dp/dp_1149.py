# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 04:54:53 2019

@author: Rekt77
"""
import sys

def dynamic(dp,N,prices):
    
    for i in range(N):
        
        if i == 0:
            dp[i][0] = prices[i][0]
            dp[i][1] = prices[i][1]
            dp[i][2] = prices[i][2]
            continue
        #R 시작        
        dp[i][0] = prices[i][0] + min(dp[i-1][1],dp[i-1][2])
        #B 시작
        dp[i][1] = prices[i][1] + min(dp[i-1][0],dp[i-1][2])
        #C 시작
        dp[i][2] = prices[i][2] + min(dp[i-1][0],dp[i-1][1])
        
    return dp[N-1]

N = int(input().strip())
prices = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
#prices = [list(map(int,input().strip().split())) for _ in range(N)]
dp = [[0,0,0] for _ in range(N)]
print(min(dynamic(dp,N,prices)))
