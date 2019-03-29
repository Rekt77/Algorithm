# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 05:23:07 2019

@author: Rekt77
"""

import sys

combination = [1,2,4,7,False,False,False,False,False,False]
testcase = list()
N = int(input().strip())

for _ in range(N):
    testcase.append(int(sys.stdin.readline().strip()))
    
for each in testcase:
    for i in range(4,each):
        if not combination[i]:
            curr = combination[i-1]+combination[i-2]+combination[i-3]
            combination[i] = curr

    print(combination[each-1])
