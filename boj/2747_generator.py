# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 01:06:23 2019

@author: Rekt77
"""
import sys
from itertools import islice

def Fibonacci_numbers():
    prev, curr = 0,1
    while True:
        yield curr
        prev, curr = curr, prev+curr
        
if __name__ == "__main__":
    f = Fibonacci_numbers()
    n = int(sys.stdin.readline().strip())
    print(list(islice(f,0,n))[n-1])