# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 05:57:51 2019

@author: Rekt77
"""
import sys

def Calculator(tables):
    counter = 0
    start = 0
    for time in tables:
        if time[0] >= start:
            start = time[1]
            counter +=1
    return counter
    
if __name__ == "__main__":
    conference = int(sys.stdin.readline().strip())
    tables = list()
    
    for _ in range(conference):
        time = tuple(map(lambda x : int(x),sys.stdin.readline().strip().split()))
        tables.append(time)

    tables = sorted(tables,key=lambda x:x[0])
    tables = sorted(tables,key=lambda x:x[1])

    print(Calculator(tables))