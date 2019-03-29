# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 17:28:16 2019

@author: ReKt77
"""

num = int(input())
queue = sorted(list(map(lambda x : int(x),input().split())))
total = 0
mySum = lambda x : sum(x)
for i in range(num):
    total += mySum(queue[:i+1])
    
print(total)